// This is the SIP specification of pyqt5_enable_new_onexit_scheme().
//
// Copyright (c) 2019 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt5.
// 
// This file may be used under the terms of the GNU General Public License
// version 3.0 as published by the Free Software Foundation and appearing in
// the file LICENSE included in the packaging of this file.  Please review the
// following information to ensure the GNU General Public License version 3.0
// requirements will be met: http://www.gnu.org/copyleft/gpl.html.
// 
// If you do not wish to use this file under the terms of the GPL version 3.0
// then you may purchase a commercial license.  For more information contact
// info@riverbankcomputing.com.
// 
// This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
// WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


%ModuleHeaderCode
bool pyqt5_get_scheme_state();
bool pyqt5_set_scheme_state(bool enabled);
%End


%ModuleCode
static bool pyqt5_scheme_state = false;

bool pyqt5_get_scheme_state()
{
    return pyqt5_scheme_state;
}

bool pyqt5_set_scheme_state(bool enabled)
{
    bool old_state = pyqt5_scheme_state;
    pyqt5_scheme_state = enabled;

    return old_state;
}
%End


bool pyqt5_enable_new_onexit_scheme(bool);
%MethodCode
    sipRes = pyqt5_set_scheme_state(a0);
%End
