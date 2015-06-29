"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------

Hook that gets executed every time a new tank instance is created.

"""

from tank import Hook
import sys
import os
import re

class TankInit(Hook):

    def execute(self, **kwargs):
        """
        Gets executed when a new Tank instance is initialized.
        """
        # Define TANK_ROOT env var used in yml config files
        tank_root = self.parent.pipeline_configuration.get_path()
        os.environ['PIPELINE_CONFIG'] = tank_root

        # Set sitecustomize
        if 'win32' in sys.platform:
            os.environ['PYTHONPATH'] = '%s;D:/Gdrive/studios/Scott Ballard/src/sitecustomize' % os.getenv('PYTHONPATH')
        elif 'darwin' in sys.platform:
            os.environ['PYTHONPATH'] = '%s;/skynet/data/Tools/Pipeline/sitecustomize' % os.getenv('PYTHONPATH')
        elif 'linux' in sys.platform:
            os.environ['PYTHONPATH'] = '%s;/mnt/skynet/data/Tools/Pipeline/sitecustomize' % os.getenv('PYTHONPATH')

        # Used to find studio apps/engine install
        os.environ['TANK_ROOT'] = re.sub('\\\\[a-zA-Z0-9]{3}\\\\tank$', '', tank_root)
        print'tank_root:', tank_root

        # Hiero network path
        if 'win32' in sys.platform:
#             os.environ['HIERO_PLUGIN_PATH'] = r'\\skynet\data\Tools\Pipeline\fac\apps\hiero'
            os.environ['HIERO_PLUGIN_PATH'] = r'D:\Gdrive\studios\CBS Digital\src\Pipeline\fac\apps\hiero'
        elif 'darwin' in sys.platform:
            os.environ['HIERO_PLUGIN_PATH'] = '/skynet/data/Tools/Pipeline/fac/apps/hiero'
        elif 'linux' in sys.platform:
            os.environ['HIERO_PLUGIN_PATH'] = '/mnt/skynet/data/Tools/Pipeline/fac/apps/hiero'

        # Hiero OCIO library
        if 'win32' in sys.platform:
            os.environ['OCIO'] = r'\\skynet\data\Tools\SOFTWARE\VFX\OpenColorIO\configs\cbsd\config.ocio'
        elif 'darwin' in sys.platform:
            os.environ['OCIO'] = '/skynet/data/Tools/SOFTWARE/VFX/OpenColorIO/configs/cbsd/config.ocio'
        elif 'linux' in sys.platform:
            os.environ['OCIO'] = '/mnt/skynet/data/Tools/SOFTWARE/VFX/OpenColorIO/configs/cbsd/config.ocio'

        # end - sb
