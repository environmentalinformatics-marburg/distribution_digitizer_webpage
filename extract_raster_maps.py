"""
extract_raster_maps.py

This is one the main files. On the one hand it defines a lot of useful
functions to manipulates scanned images and can thus be imported as a module.
One the other hand it can be exectued as a script and extract all the maps
present on the input page, clips them, extract the page number from the head
and saves the output images under the name <page number>_<map number>.

Usage:
    python extract_raster_maps.py <input scanned page> --output_dir <output directory>
"""
# First of all, on top of any python source files, the imports
#
# os: for file and path names manipulations and basic OS stuff such as create
# directories
import os
# re: Regular expressions. A world on its own
import re
# PIL: Python Image Library, low level image manipulation
from PIL import Image
# Numpy: numeric arrays, we need them all the time
import numpy as np
# This is a wrapper around Googles Optical Character Recognition software
import pytesseract
# Managing command line arguments when executed as a script
import argparse
# Useful function for signal processing
import scipy.signal as signal

# Define a home made error to be able to signal problems.
# This is the most basic one... Just don't worry about it, you get a feeling of
# why you should need it only after having written a couple of big scripts...
class Fehler(Exception):
    pass

def block_ranges(a, x):
    """Find blocks of consecutive values greater than x in array a.

    Return an array of shape (number of blocks, 2) containing the indices of
    begin and end (+1) of each block.

    This function is meant to find white blocks to split features on a scanned
    page.
    """
    # Create an array that is 1 where a > x, and pad each end with an extra 0.
    iszero = np.concatenate(([0], np.greater_equal(a, x).view(np.int8), [0]))
    # Create an array which is 1 everytime the previous one changes value.
    # Hence the following array is 1 at each beginning and end of the desired
    # blocks
    absdiff = np.abs(np.diff(iszero))

    # Find the indices where the previous array is 1. We get a list of even
    # length containing the indices of begin and end of the blocks we look for:
    # [beg1, end1, beg2, end2, ...]
    #
    # Reshape the above list to get the form:
    # [[beg1, end1],
    #  [beg2, end2],
    #  ...]
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    return ranges

# The following function is the same as the previous one, except that it finds
# blocks of values *smaller* than a given threshold x.
def block_ranges2(a, x):
    """Find blocks of consecutive values lower than x in array a.

    Return an array of shape (number of blocks, 2) containing the indices of
    begin and end (+1) of each block.

    This function is means to find black blocks.
    """
    # Create an array that is 1 where a < x, and pad each end with an extra 0.
    # the "np.less_equal(...)" below is the only difference with the function
    # above.
    iszero = np.concatenate(([0], np.less_equal(a, x).view(np.int8), [0]))
    absdiff = np.abs(np.diff(iszero))
    # Runs start and end where absdiff is 1.
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    return ranges


def remove_head(img, th=254.9, min_size=50):
    """Returns head, body.
    
    Splits the head from the body of the page and return both. The head is
    simply the first horizontal black block.
    """
    # Make a horizontal mean fo the picture. The following array is 255
    # everytime there is a line of completely white pixels.
    m = img.mean(axis=1)
    # Get the indices of the black blocks.
    blocks = block_ranges2(m, th)
    # Get the sizes of the blocks. The size of a block starting at beg and
    # ending at end is end - beg. Due to the shape of the output of
    # block_ranges2, we get a column containing the sizes of the blocks with:
    # diff(blocks, axis=1). The output of this is of shape (number of blocks,
    # 1), i.e. it has many lines and one column, but it is still a 2D array. To
    # "flatten" it, we apply the .ravel() method (which just flattens an
    # array).
    sizes = np.diff(blocks, axis=1).ravel()
    # Get the first block of size bigger than min_size:
    # blocks[sizes > min_size] are all the blocks of size greater than
    # min_size.
    # With the [0] we take the first in the list.
    # Since blocks is 2D, any blocks[i] is a 1D array. Specifically, each
    # blocks[i] has length 2. To unpack it, we can do:
    # a, b = blocks[i]
    # This is synonymous to
    # >>> a = blocks[i, 0]
    # >>> b = blocks[i, 1]
    # but is more concise and readable.
    # So we do it
    beg_head, end_head = blocks[sizes > min_size][0]

    # We return a tuple of two elements.  The first is the head: here we return
    # the (end_head + 20) first rows of the image.
    # The second is the body: these are the (end_head + 50) last rows
    # The 20 and 50 are arbitrary and are so that we don't cut too much of the
    # head...
    return img[:end_head + 20], img[end_head + 50:]


def get_page_number(head):
    """Returns the page number read from the head.

    If there is no text in the head, raise an Exception
    """
    # Get the text
    # The image_to_string function from the pytesseract module expects an Image
    # instance from the PIL module. Here, we construct it from the array
    # containing the head of the page. The final .replace is there to eliminate
    # white spaces, because sometimes, whitespaces are inserted in the middle
    # of the page number
    head_text = pytesseract.image_to_string(Image.fromarray(head)).replace(' ', '')
    # Check if no text was extracted, i.e. if the string obtained has length = 0
    if len(head_text) == 0:
        # If no text was found, raise an error and exit
        raise Fehler("""No head, skipping""")
    # In our case, the page number is the first 3 characters found
    page_number = head_text[:3]
    # Return the int version. If the string is not a number, an error will be
    # raise.
    return int(page_number)

# The following function is not actually used by any script, but I had used it
# to extract the butterfly names.
def split_paragraphs(body, th=246, min_size=150):
    """Returns a list of imgs correponding to the paragraphs.
    
    Here, we need a lower threshold in case there is a map in the margin.
    """
    # Get the mean
    m = body.mean(axis=1)
    # Get the blocks
    white_blocks = block_ranges(m, th)
    # Get the block sizes
    block_sizes = np.diff(white_blocks, axis=1).ravel()
    # Select the ones we want
    to_take = block_sizes > min_size
    # Insert a zero for the first paragraph
    blocks = np.insert(white_blocks[to_take], 0, [0, 50], axis=0)
    # The beginnings and ends of the white blocks
    begs, ends = blocks.T

    # Due to the low threshold, we loose some text. To correct this, we take
    # some of the white block back
    return [body[end-50:beg] for beg, end in zip(begs[1:], ends[:-1])]

# This function is very important: it splits the text and the maps columns in
# one page
def split_columns(img, th=253.5, min_size=600, margins=100):
    """Returns img_col, text_col"""
    # A column is a vertical feature so we have to do a vertical mean to
    # identify the non white columns
    m = img.mean(axis=0)
    # Find the non white columns
    blocks = block_ranges2(m, th)
    # Get the block sizes: we will only select non white columns larger than
    # some minimum size in order not to get small scan rubbish
    block_sizes = np.diff(blocks, axis=1).ravel()
    # Get the indices of the beginning and end of the columns
    columns = blocks[block_sizes > min_size]
    # Check the number of columns found
    if len(columns) == 1:
        # If we got only one, probably there is no map. Still we have to return
        # something for the map column, so we just return some array with zero,
        # the subsequent function looking for maps will then find none.
        (beg, end), = columns
        return np.array([[0]]), img[:,beg:end]
    elif len(columns) == 2:
        # If we got 2 columns, perfect. The first column will be for maps and
        # the second for the text.
        # Get the indices of start and end of the columns
        beg1, end1 = columns[0]
        beg2, end2 = columns[1]
        # Return the couple of columns. For the maps, we add some margins in
        # order to be sure not to cut them.  They will be clipped anyway after
        # that.
        return img[:, beg1-margins:end1+margins], img[:, beg2:end2]
    else:
        # Problem, raise an error.
        raise Felher("""No columns found""")

# This function is not used either.  It is meant to extract the names of the
# butterfly from the paragraphs
def extract_names(img):
    """Return the name from the paragraph."""
    # Get the text from the paragraph
    thetext = pytesseract.image_to_string(Image.fromarray(img))
    # Regular expression to match lines starting with a number
    # See the notebook with the regular expression
    myre = '^\d+\..+'
    # look for the regular expression
    lines = re.findall(myre, thetext, flags=re.MULTILINE)
    # Get the two first words after the number, and join them with '_'
    return ['_'.join(s.split()[1:3]) for s in lines]

def get_maps(img, th=253.5, min_size=650):
    """Returns a list containing the maps.
    
    Expects a maps column as image and look for vertical non white blocks."""
    m = img.mean(axis=1)
    blocks = block_ranges2(m, th)
    block_sizes = np.diff(blocks, axis=1).ravel()

    # Return only the blocks bigger than some minimum size
    return [img[a:b] for a, b in blocks[block_sizes > min_size]]

# This function is really not so good, I think in the end I defined all my
# threshold ad hoc.
def estimate_threshold(m):
    """Returns an estimation of the threshold for white blocks."""
    def amount_of_white(m, th):
        white_blocks = block_ranges(m, th)
        blocks_sizes = np.diff(white_blocks, axis=1).ravel()
        return blocks_sizes.sum()

    thresholds = np.linspace(250, 255, 100)
    amounts_of_white = np.array([amount_of_white(m, th) for th in thresholds])
    # The last line is not elegant. Hopefully it works!
    return thresholds[np.diff(amounts_of_white).argmin()]

# This function is simple but important: it clips the maps along a given
# direction: horizontally or vertically (controlled by the axis parameter
def clip_map(img, th=None, axis=0):
    # Get the mean along the desired axis
    m = img.mean(axis=axis)
    if th is None:
        # If no threshold is given, estimate it. Not recommended.
        th = estimate_threshold(m)
    if axis == 1:
        # If we clip horizontally, then we have to return rows. We return all
        # the non white rows.
        return img[m < th]
    elif axis == 0:
        # If we clip vertically, then we return all the non white columns.
        return img[:, m < th]



# Everything after the following line gets executed only the file is executed
# as a script. So it is possible to import all the previous functions in other
# scripts, or to run this script to do the following.
#
# This script cuts the head and gets the page number,
# then splits the columns
# finally, from the map column, splits the maps and saves them as png.
if __name__ == '__main__':
    # Parse command line arguments. This means extract them and transform them
    # into variables we can use in the script
    #
    # Create the parser object
    parser = argparse.ArgumentParser()
    # Add a positional argument, here the path to the input image
    parser.add_argument('image')
    # Add an optional argument, this one is the directory where to store the
    # extracted maps. We define a default value which is the current directory
    # in this case.
    parser.add_argument('--output_dir', default='.')
    # Parse the arguments, i.e. collect them in a usable form.
    args = parser.parse_args()
    # Just rename them for convenience.
    img_path = args.image
    outdir = args.output_dir

    # Check if the output directory exists.
    if not os.path.exists(outdir):
        # If not, create it
        os.mkdir(outdir)

    # Open the input image. In the other scripts I use scipy.ndimage.imread
    # which I would recomend more than PIL. The output is the same.
    img = Image.open(img_path)
    width, height = img.size
    # The img_array is a 2D array of int between 0 and 255 indicating the
    # grayscale values of the pixels
    img_array = np.array(img.getdata(), dtype=np.uint8).reshape(height, width)

    # Split the head
    head, img_array = remove_head(img_array, th=254.5)
    # The page number 374 just doesn't get regognized, so I just manage it
    # manually
    if img_path == 'scantailor_output/doc02356520160503142644_004_1L.tif':
        page = 374
    else:
        page = get_page_number(head)
    # the following line is just a check when running the script manually.
    print(page)

    # low threshold + margins
    col_th = 254
    margins = 100
    # split the columns
    col_imgs, col_txt = split_columns(img_array, th=col_th, margins=margins)

    # define threshold. We can afford it very high because the images are black
    # and white.
    maps_th = 254.9
    # Get the maps
    maps = get_maps(col_imgs, th=maps_th)

    clip_th = 254.6
    # Iterate on the found maps
    # When using the enumerate iterator, we get the index of the iteration
    for n, m in enumerate(maps):
        # Create the output name.
        outname = os.path.join(outdir, '{p}_{n}.png'.format(p=page,n=n))
        # clip around both axes
        clipped = clip_map(clip_map(m, th=clip_th, axis=0), th=clip_th, axis=1)
        # Save the image
        Image.fromarray(clipped).save(outname)
        # Also create a file containing the name of the original name of the
        # scanned page.  This is for back checking if something goes wrong.
        with open(outname + '.original_page', 'w') as f:
            f.write(os.path.basename(img_path))
