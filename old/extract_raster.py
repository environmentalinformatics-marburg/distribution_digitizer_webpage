
# coding: utf-8

if __name__ == '__main__':
    import argparse
    import os
    import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as collections
import matplotlib.image as mpimg
from scipy.spatial import Delaunay
import shapely.ops as ops
import shapely.geometry as geometry
import seaborn as sns

def alpha_hull_2D(points, alpha):
    """
    Calculate the alpha hull of a set of 2D points.

    Parameters
    ----------
    points: np.array of shape (N, 2)
        Basically a list of points.
    alpha: float
        If alpha = 0, then the alpha hull is the convex hull. For increasing
        alpha, the hull gets tighter and tighter.

    Returns
    -------
    hull: shapely.geometry.MultiLineString or shapely.geometry.LineString
        Object containing all the parts of the hull. If the hull is in one
        part, then a LineString is returned.
    """
    def circumcircle_r(triangle):
        """
        Calculates the radius of the circum cricle of the triangle.

        The formula use is:
        radius = product of the lengthes of the faces / (4 * area)
        
        Parameters
        ----------
        triangle: np.array of shape (3, 2, N) or (3, 2)
            Array containing the coordinates of the three points of N
            triangles.

        Returns
        -------
        radius: np.array of shape (N,)
            List of the radii of the circles circumscripted around the
            triangles.
        """
        if triangle.ndim == 2:
            triangle = triangle[:,:,np.newaxis]
        face_vectors = triangle[[-1, 0, 1]] - triangle
        
        _, _, n = face_vectors.shape
        a, b, c, d = face_vectors[1:].reshape(4, n)
        double_area = abs(a*d - b*c)
        
        face_lengths = np.linalg.norm(face_vectors, axis=1)
        
        return face_lengths.prod(axis=0) / (2.0 * double_area)
    
    delaunay = Delaunay(points)
    triangles = np.transpose(points[delaunay.simplices], axes=(1, 2, 0))
    circ_circle_radius = circumcircle_r(triangles)
    to_pick = circ_circle_radius < 1.0 / alpha
    
    triangles = [geometry.Polygon(triangle) for triangle 
                 in points[delaunay.simplices[to_pick]]]
    alpha_polygon = ops.cascaded_union(triangles)
    return alpha_polygon.boundary



def polyplot(poly, ax=None, autolim=False, gca_kwargs={}, *args, **kwargs):
    if ax is None:
        ax = plt.gca(**gca_kwargs)
    if autolim:
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        a, b, c, d = poly.bounds
        if xmin > a:
            xmin = a
        if ymin > b:
            ymin = b
        if xmax < c:
            xmax = c
        if ymax < d:
            ymax = d
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)
    patch = patches.Polygon(poly, *args, **kwargs)
    ax.add_patch(patch)
    return ax

if __name__ == '__main__':
    # Parse commandline arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("picture")
    parser.add_argument("--alpha", type=float, default=1.0)
    parser.add_argument("--threshold", type=int, default=90)
    parser.add_argument("--minsize", type=float, default=10.0)
    args = parser.parse_args()

    # Names of output files
    basename, _ = os.path.splitext(args.picture)
    out_map = basename + '.pdf'
    out_txt = basename + '.txt'
    out_js = basename + '.js'

    # Get interresting pixels
    img = mpimg.imread(args.picture)
    raster_pixels = img < args.threshold
    th_black = 200
    black_pixels = img < th_black

    # Get the coordinate of all black pixels
    xb, yb = np.where(black_pixels)

    # Get coordinates of raster pixels
    x, y = np.where(raster_pixels)
    points = np.array([x, y]).transpose()
    # Calculate the Hull around those points
    hulls = [a for a in alpha_hull_2D(points, alpha=args.alpha) if a.length >
            args.minsize]
    # Extract the coordinates of the points composing the hull
    hulls_coords = np.vstack([np.asarray(hull, dtype=int) for hull in hulls])
    # Save the coordinates in txt and json
    np.savetxt(out_txt, hulls_coords, fmt='%d')
    with open(out_js, 'w') as f:
        json.dump(hulls_coords.tolist(), f, indent=4, separators=(',', ':'))

    # white style for plotting
    sns.set_style("white")
    # Getting some colors for plotting
    blue, green, red = sns.color_palette(palette='pastel', n_colors=3, desat=0.5)

    # Plotting the "right" way, only hick: x and y axis are exchanged
    fig, ax = plt.subplots(figsize=(10,10))
#    ax.invert_xaxis()
#    ax.invert_yaxis()
    ax.scatter(xb, yb, marker='.', c='black')
    for h in hulls:
        polyplot(h, ax=ax, edgecolor=red, linewidth=3, facecolor=blue, alpha=0.5)
    fig.savefig(out_map)


    # This is not very good: I'm recreating an image, instead of plotting the
    # points.
#    length, width = img.shape
#    imgres = (np.ones((length, width, 3)) * img[:,:,np.newaxis]) / 255
#    imgres[raster_pixels] = green
#
#    hx, hy = hulls_coords.transpose()
#
#    imgres[hx, hy] = 0, 0, 1
#
#    sns.set_style("white")
#    fig = plt.figure(figsize=(10,10))
#    plt.imshow(imgres)
#    fig.savefig(out_map)

    
