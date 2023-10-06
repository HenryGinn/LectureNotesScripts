from hgutilities import defaults
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from line import Line

class Lattice():

    def __init__(self, **kwargs):
        self.process_kwargs(kwargs)
        self.set_geometry()
        self.set_spatial_limits()
        self.create_figure()
        self.add_primitive_lines()

    def process_kwargs(self, kwargs):
        defaults.kwargs(self, kwargs)
        self.set_type()

    def set_type(self):
        self.set_type_function_dict()
        if self.type is not None:
            self.type_function_dict[self.type]()

    def set_type_function_dict(self):
        self.type_function_dict = (
            {"Cubic": self.set_type_cubic,
             "Orthohombic": self.set_type_orthohombic,
             "Hexagonal": self.set_type_hexagonal,
             "Trigonal": self.set_type_trigonal,
             "Triclininc": self.set_type_triclinic,
             "Monoclinic": self.set_type_monoclinic,
             "Rhombohedral": self.set_type_rhombohedral})

    def set_type_cubic(self):
        self.size_x, self.size_y, self.size_z = 1, 1, 1
        self.angle_xy, self.angle_yz, self.angle_zx = 90, 90, 90
        self.length_x, self.length_y, self.length_z = 1, 1, 1

    def set_type_orthohombic(self):
        self.size_x, self.size_y, self.size_z = 1, 1, 1
        self.angle_xy, self.angle_yz, self.angle_zx = 90, 90, 90
        self.length_x, self.length_y, self.length_z = 1, 1, 1

    def set_type_hexagonal(self):
        self.size_x, self.size_y, self.size_z = 1, 1, 1
        self.angle_xy, self.angle_yz, self.angle_zx = 90, 90, 90
        self.length_x, self.length_y, self.length_z = 1, 1, 1

    def set_type_trigonal(self):
        self.size_x, self.size_y, self.size_z = 1, 1, 1
        self.angle_xy, self.angle_yz, self.angle_zx = 90, 90, 90
        self.length_x, self.length_y, self.length_z = 1, 1, 1

    def set_type_triclinic(self):
        self.size_x, self.size_y, self.size_z = 1, 1, 1
        self.angle_xy, self.angle_yz, self.angle_zx = 90, 90, 90
        self.length_x, self.length_y, self.length_z = 1, 1, 1

    def set_type_monoclinic(self):
        self.size_x, self.size_y, self.size_z = 1, 1, 1
        self.angle_xy, self.angle_yz, self.angle_zx = 90, 90, 90
        self.length_x, self.length_y, self.length_z = 1, 1, 1

    def set_type_rhombohedral(self):
        self.size_x, self.size_y, self.size_z = 1, 1, 1
        self.angle_xy, self.angle_yz, self.angle_zx = 90, 90, 90
        self.length_x, self.length_y, self.length_z = 1, 1, 1

    def set_geometry(self):
        self.set_limits()
        self.set_base_vectors()
        self.set_base_vertices()

    def set_limits(self):
        origin_x = self.set_limits_x()
        origin_y = self.set_limits_y()
        origin_z = self.set_limits_z()
        self.origin = np.array([origin_x, origin_y, origin_z])

    def set_limits_x(self):
        if self.size_x % 2 == 0:
            return self.set_limits_x_even()
        else:
            return self.set_limits_x_odd()

    def set_limits_x_even(self):
        self.x_limit_min = -int(self.size_x / 2)
        self.x_limit_max = int(self.size_x / 2)
        origin_x = 0
        return origin_x

    def set_limits_x_odd(self):
        self.x_limit_min = -int((self.size_x - 1) / 2)
        self.x_limit_max = int((self.size_x + 1) / 2)
        origin_x = -0.5
        return origin_x

    def set_limits_y(self):
        if self.size_y % 2 == 0:
            return self.set_limits_y_even()
        else:
            return self.set_limits_y_odd()

    def set_limits_y_even(self):
        self.y_limit_min = -int(self.size_y / 2)
        self.y_limit_max = int(self.size_y / 2)
        origin_y = 0
        return origin_y

    def set_limits_y_odd(self):
        self.y_limit_min = -int((self.size_y - 1) / 2)
        self.y_limit_max = int((self.size_y + 1) / 2)
        origin_y = -0.5
        return origin_y

    def set_limits_z(self):
        if self.size_z % 2 == 0:
            return self.set_limits_z_even()
        else:
            return self.set_limits_z_odd()

    def set_limits_z_even(self):
        self.z_limit_min = -int(self.size_z / 2)
        self.z_limit_max = int(self.size_z / 2)
        origin_z = 0
        return origin_z

    def set_limits_z_odd(self):
        self.z_limit_min = -int((self.size_z - 1) / 2)
        self.z_limit_max = int((self.size_z + 1) / 2)
        origin_z = -0.5
        return origin_z

    def set_base_vectors(self):
        self.base_x = np.array([1, 0, 0])
        self.base_y = np.array([np.cos(np.pi/180*self.angle_xy),
                                np.sin(np.pi/180*self.angle_xy), 0])
        self.set_base_z()
        self.round_basis_vectors()

    def set_base_z(self):
        self.base_z = np.array([np.cos(np.pi/180*self.angle_zx),
                                np.cos(np.pi/180*self.angle_yz)*np.sin(np.pi/180*self.angle_zx),
                                np.sin(np.pi/180*self.angle_yz)*np.sin(np.pi/180*self.angle_zx)])

    def round_basis_vectors(self):
        self.base_x = np.round(self.base_x, 5)
        self.base_y = np.round(self.base_y, 5)
        self.base_z = np.round(self.base_z, 5)

    def set_base_vertices(self):
        self.base_vertices = [self.get_base_vertex(x, y, z)
                              for x in range(self.x_limit_min, self.x_limit_max + 1)
                              for y in range(self.y_limit_min, self.y_limit_max + 1)
                              for z in range(self.z_limit_min, self.z_limit_max + 1)]

    def get_base_vertex(self, x, y, z):
        vertex = (self.origin +
                  x * self.base_x +
                  y * self.base_y +
                  z * self.base_z)
        return vertex

    def set_spatial_limits(self):
        self.set_spatial_limits_x()
        self.set_spatial_limits_y()
        self.set_spatial_limits_z()

    def set_spatial_limits_x(self):
        self.normal_x = np.cross(self.base_y, self.base_z)
        self.spatial_x_min = self.get_spatial_limit(
            self.x_limit_min, self.base_x, self.normal_x)
        self.spatial_x_max = self.get_spatial_limit(
            self.x_limit_max, self.base_x, self.normal_x)

    def set_spatial_limits_y(self):
        self.normal_y = np.cross(self.base_z, self.base_x)
        self.spatial_y_min = self.get_spatial_limit(
            self.y_limit_min, self.base_y, self.normal_y)
        self.spatial_y_max = self.get_spatial_limit(
            self.y_limit_max, self.base_y, self.normal_y)

    def set_spatial_limits_z(self):
        self.normal_z = np.cross(self.base_x, self.base_y)
        self.spatial_z_min = self.get_spatial_limit(
            self.z_limit_min, self.base_z, self.normal_z)
        self.spatial_z_max = self.get_spatial_limit(
            self.z_limit_max, self.base_z, self.normal_z)

    def get_spatial_limit(self, constant, basis, normal):
        extreme_point = self.origin + constant*basis
        plane_constant = np.dot(extreme_point, normal)
        return plane_constant

    def create_figure(self):
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig, auto_add_to_figure=False)
        self.fig.add_axes(self.ax)
        self.ax.set_axis_off()

    def add_primitive_lines(self):
        self.lines = [Line(self, (0, 0, 0), (1, 0, 0)),
                      Line(self, (0, 0, 0), (0, 1, 0)),
                      Line(self, (0, 0, 0), (0, 0, 1))]

    def draw(self):
        self.collect_facets()
        self.draw_vertices()
        self.draw_edges()
        plt.show()

    def collect_facets(self):
        self.collect_vertices()
        self.collect_edges()

    def collect_vertices(self):
        self.vertices = [vertex for line in self.lines
                         for vertex in line.vertices]
        self.vertices = list(set(self.vertices))
        
    def collect_edges(self):
        self.edges = [edge for line in self.lines
                         for edge in line.edges]
        self.edges = list(set(self.edges))

    def draw_vertices(self):
        for vertex in self.vertices:
            self.ax.plot(*vertex, "ko")

    def draw_edges(self):
        for edge in self.edges:
            edge_xyz = list(zip(*edge))
            self.ax.plot(*edge_xyz, color="black")

defaults.load(Lattice)