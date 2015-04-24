##
# Copyright 2014 Petar Forai
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
CrayCCE toolchain: Cray compilers (CCE) and MPI via Cray compiler drivers + LibSci (PrgEnv-cray) and Cray FFTW

@author: Petar Forai (IMP/IMBA, Austria)
@author: Kenneth Hoste (Ghent University)
"""
from easybuild.toolchains.compiler.craype import CrayPECray
from easybuild.toolchains.fft.crayfftw import CrayFFTW
from easybuild.toolchains.linalg.libsci import LibSci
from easybuild.toolchains.mpi.craype import CrayPEMPI


class CrayCCE(CrayPECray, CrayPEMPI, LibSci, CrayFFTW):
    """Compiler toolchain for Cray Programming Environment for Cray Compiling Environment (CCE) (PrgEnv-cray)."""
    NAME = 'CrayCCE'

    def prepare(self, *args, **kwargs):
        """Prepare to use this toolchain; marked as experimental."""
        super(CrayCCE, self).prepare(*args, **kwargs)
        self.log.experimental("%s toolchain", self.NAME)
