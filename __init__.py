# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EcoRes
                                 A QGIS plugin
  This plugin calculates ecosystem respiration from thermal images.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-02-07
        copyright            : (C) 2021 by Florian Ellsäßer
        email                : el-flori@gmx.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load EcoRes class from file EcoRes.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ecores import EcoRes
    return EcoRes(iface)