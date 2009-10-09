# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2009 Guillaume Pellerin <yomguy@parisson.com>

# This file is part of TimeSide.

# TimeSide is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# TimeSide is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with TimeSide.  If not, see <http://www.gnu.org/licenses/>.

# Author: Guillaume Pellerin <yomguy@parisson.com>

from timeside.analyze.core import *
from timeside.analyze.api import IAnalyzer
import numpy

class ResolutionAnalyser(AudioProcessor):
    """Media item analyzer driver interface"""

    implements(IAnalyzer)

    def get_id(self):
        return "resolution"

    def get_name(self):
        return "Resolution"

    def get_unit(self):
        return "bits"

    def render(self, media_item, options=None):
        self.pre_process(media_item)
        if '8' in self.encoding:
            return 8
        if '16' in self.encoding:
            return 16
        if '24' in self.encoding:
            return 24
        if '32' in self.encoding:
            return 32
        else:
            return ''