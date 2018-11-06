# Copyright (C) 2016-2018 Christian Fetzer
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

""" Libretro core configuration

    Override settings for specific libretro cores. """

# pylint: disable=bad-whitespace, line-too-long
# flake8: noqa

GITHUB_ORGANIZATION = 'kodi-game'
GITHUB_ADDON_PREFIX = 'game.libretro.'

# core: {(Libretro repo, Makefile, Directory)}
ADDONS = {
    '2048':                      ('libretro-2048',              'Makefile.libretro', '.',                 'jni'),
    '4do':                       ('4do-libretro',               'Makefile',          '.',                 'jni'),
    'beetle-bsnes':              ('beetle-bsnes-libretro',      'Makefile',          '.',                 'jni', {'soname': 'mednafen_snes'}),
    'beetle-gba':                ('beetle-gba-libretro',        'Makefile',          '.',                 'jni', {'soname': 'mednafen_gba'}),
    'beetle-lynx':               ('beetle-lynx-libretro',       'Makefile',          '.',                 'jni', {'soname': 'mednafen_lynx'}),
    'beetle-ngp':                ('beetle-ngp-libretro',        'Makefile',          '.',                 'jni', {'soname': 'mednafen_ngp'}),
    'beetle-pce-fast':           ('beetle-pce-fast-libretro',   'Makefile',          '.',                 'jni', {'soname': 'mednafen_pce_fast'}),
    'beetle-pcfx':               ('beetle-pcfx-libretro',       'Makefile',          '.',                 'jni', {'soname': 'mednafen_pcfx'}),
    'beetle-psx':                ('beetle-psx-libretro',        'Makefile',          '.',                 'jni', {'soname': 'mednafen_psx'}),
    'beetle-saturn':             ('beetle-saturn-libretro',     'Makefile',          '.',                 'jni', {'soname': 'mednafen_saturn'}),
    'beetle-supergrafx':         ('beetle-supergrafx-libretro', 'Makefile',          '.',                 'jni', {'soname': 'mednafen_supergrafx'}),
    'beetle-vb':                 ('beetle-vb-libretro',         'Makefile',          '.',                 'jni', {'soname': 'mednafen_vb'}),
    'beetle-wswan':              ('beetle-wswan-libretro',      'Makefile',          '.',                 'jni', {'soname': 'mednafen_wswan'}),
    'bluemsx':                   ('blueMSX-libretro',           'Makefile',          '.',                 'jni'),
    'bnes':                      ('bnes-libretro',              'Makefile',          '.',                 'jni'),
    'bsnes-mercury-accuracy':    ('bsnes-mercury',              'Makefile',          '.',                 'target-libretro/jni', {'binary_dir': 'out', 'soname': 'bsnes_mercury_accuracy', 'jnisoname': 'libretro_bsnes_mercury_accuracy', 'cmake_options': 'profile=accuracy'}),
    'bsnes-mercury-balanced':    ('bsnes-mercury',              'Makefile',          '.',                 'target-libretro/jni', {'binary_dir': 'out', 'soname': 'bsnes_mercury_balanced', 'jnisoname': 'libretro_bsnes_mercury_balanced', 'cmake_options': 'profile=balanced'}),
    'bsnes-mercury-performance': ('bsnes-mercury',              'Makefile',          '.',                 'target-libretro/jni', {'binary_dir': 'out', 'soname': 'bsnes_mercury_performance', 'jnisoname': 'libretro_bsnes_mercury_performance', 'cmake_options': 'profile=performance'}),
    'cap32':                     ('libretro-cap32',             'Makefile',          '.'  ,               'jni'),
    'desmume':                   ('desmume',                    'Makefile.libretro', 'desmume/src/frontend/libretro', 'desmume/src/frontend/libretro/jni'),
    #'chailove':                  ('libretro-chailove',          'Makefile',          '.',                 'jni'),  # Uses Git submodules
    #'dolphin':                   ('dolphin',                    'Makefile',          'Source/Core/DolphinLibretro', 'Source/Core/DolphinLibretro/jni', {'binary_dir': 'Source/Core/DolphinLibretro'}),  # Longrunning, Switched to CMake
    'dinothawr':                 ('Dinothawr',                  'Makefile',          '.',                 'jni'),
    'dosbox':                    ('dosbox-libretro',            'Makefile.libretro', '.',                 'jni'),
    'fbalpha':                   ('fbalpha',                    'makefile.libretro', '.',                 'jni'),
    'fbalpha2012':               ('fbalpha2012',                'makefile.libretro', 'svn-current/trunk', 'svn-current/trunk/projectfiles/libretro-android/jni'),
    'fceumm':                    ('libretro-fceumm',            'Makefile',          '.',                 'jni'),
    'fmsx':                      ('fmsx-libretro',              'Makefile',          '.',                 'jni'),
    #'fsuae':                     ('libretro-fsuae',             'Makefile.libretro', '.',                 'jni', {'branch': 'libretro-fsuae'}),  # Fails to build
    'fuse':                      ('fuse-libretro',              'Makefile',          '.',                 'jni'),
    'gambatte':                  ('gambatte-libretro',          'Makefile',          '.',                 'libgambatte/libretro/jni'),
    'genplus':                   ('Genesis-Plus-GX',            'Makefile.libretro', '.',                 'libretro/jni', {'soname': 'genesis_plus_gx'}),
    'gw':                        ('gw-libretro',                'Makefile',          '.',                 'jni'),
    'handy':                     ('libretro-handy',             'Makefile',          '.',                 'jni'),
    'hatari':                    ('hatari',                     'Makefile.libretro', '.',                 'jni'),
    'lutro':                     ('libretro-lutro',             'Makefile',          '.',                 'jni'),
    'mame2000':                  ('mame2000-libretro',          'Makefile',          '.',                 'jni'),
    'mame2003':                  ('mame2003-libretro',          'Makefile',          '.',                 'jni'),
    'mame2003_plus':             ('mame2003-plus-libretro',     'Makefile',          '.',                 'jni'),
    #'mame2010':                  ('mame2010-libretro',          'Makefile',          '.',                 'jni', {'cmake_options': 'VRENDER=soft PTR64=1'}),  # Huge and longrunning
    #'mame2014':                  ('mame2014-libretro',          'Makefile',          '.',                 'jni', {'cmake_options': 'PTR64=1 TARGET=mame'}),  # Huge and longrunning
    #'mame2016':                  ('mame2016-libretro',          'Makefile.libretro', '.',                 'jni', {'cmake_options': 'PTR64=1'}),  # Huge and longrunning
    #'mame':                      ('mame',                       'Makefile.libretro', '.',                 'jni', {'cmake_options': 'PTR64=1'}),  # Huge and longrunning
    'melonds':                   ('melonDS',                    'Makefile',          '.',                 'jni'),
    'meteor':                    ('meteor-libretro',            'Makefile',          'libretro',          'libretro/jni'),
    'mgba':                      ('mgba',                       'Makefile',          '.',                 'jni'),
    'mupen64plus':               ('mupen64plus-libretro',       'Makefile',          '.',                 'jni'),
    'mrboom':                    ('mrboom-libretro',            'Makefile',          '.',                 'jni'),
    'nestopia':                  ('nestopia',                   'Makefile',          'libretro',          'libretro/jni'),
    'nx':                        ('nxengine-libretro',          'Makefile',          '.',                 'jni', {'soname': 'nxengine'}),
    'o2em':                      ('libretro-o2em',              'Makefile',          '.',                 'jni'),
    'pcem':                      ('libretro-pcem',              'Makefile.libretro', 'src',               'jni'),
    'pcsx-rearmed':              ('pcsx_rearmed',               'Makefile.libretro', '.',                 'jni', {'soname': 'pcsx_rearmed'}),
    'picodrive':                 ('picodrive',                  'Makefile.libretro', '.',                 'jni'),
    'pokemini':                  ('PokeMini',                   'Makefile.libretro', '.',                 'jni'),
    #'ppsspp':                    ('ppsspp',                     'Makefile',          'libretro',          'jni'),  # Longrunning, requires OpenGL
    'prboom':                    ('libretro-prboom',            'Makefile',          '.',                 'jni'),
    'prosystem':                 ('prosystem-libretro',         'Makefile',          '.',                 'jni'),
    'quicknes':                  ('QuickNES_Core',              'Makefile',          '.',                 'jni'),
    #'reicast':                   ('reicast-emulator',           'Makefile',          '.',                 'jni'),  # Fails to compile
    'sameboy':                   ('SameBoy',                    'Makefile',          'libretro',          'libretro/jni', {'branch': 'buildbot'}),
    #'rustation':                 ('rustation-libretro',         'Makefile',          '.',                 'jni'),  # Checkout fails
    'scummvm':                   ('scummvm',                    'Makefile',          'backends/platform/libretro/build', None, {'binary_dir': 'backends/platform/libretro/build'}),
    'snes9x':                    ('snes9x',                     'Makefile',          'libretro',          'libretro/jni'),
    'snes9x2002':                ('snes9x2002',                 'Makefile',          '.',                 'jni'),
    'snes9x2010':                ('snes9x2010',                 'Makefile',          '.',                 'jni'),
    'stella':                    ('stella-libretro',            'Makefile',          '.',                 'jni'),
    'tgbdual':                   ('tgbdual-libretro',           'Makefile',          '.',                 'jni'),
    'tyrquake':                  ('tyrquake',                   'Makefile',          '.',                 'jni'),
    'uae':                       ('libretro-uae',               'Makefile',          '.',                 'jni', {'soname': 'puae'}),
    #'uae4arm':                   ('uae4arm-libretro',           'Makefile',          '.',                 'jni'),  # Fails to build on non arm system
    'vbam':                      ('vbam-libretro',              'Makefile',          'src/libretro',      'src/libretro/jni'),
    'vba-next':                  ('vba-next',                   'Makefile',          '.',                 'libretro/jni', {'soname': 'vba_next'}),
    'vecx':                      ('libretro-vecx',              'Makefile',          '.',                 'jni'),
    'vice':                      ('vice-libretro',              'Makefile.libretro', '.',                 'jni', {'soname': 'vice_x64'}),
    'yabause':                   ('yabause',                    'Makefile',          'libretro',          'libretro/jni'),
    'virtualjaguar':             ('virtualjaguar-libretro',     'Makefile',          '.',                 'jni')
}
