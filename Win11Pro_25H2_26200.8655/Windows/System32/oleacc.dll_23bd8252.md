# Binary Specification: oleacc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\oleacc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `23bd8252af830db88ad6d229b06e4fd192dabedcbb9bfaa9fc9a85b1ad654909`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `GetProcessHandleFromHwnd` | `0x4660` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `DllGetClassObject` | `0x4800` | 396 | UnwindData |  |
| 10 | `AccessibleObjectFromWindowTimeout` | `0x4DA0` | 3,140 | UnwindData |  |
| 7 | `AccessibleObjectFromEvent` | `0x6F50` | 430 | UnwindData |  |
| 27 | `PropMgrClient_LookupProp` | `0xC2A0` | 143 | UnwindData |  |
| 9 | `AccessibleObjectFromWindow` | `0xFA80` | 67 | UnwindData |  |
| 25 | `LresultFromObject` | `0x12F00` | 62 | UnwindData |  |
| 6 | `AccessibleChildren` | `0x14830` | 40 | UnwindData |  |
| 11 | `CreateStdAccessibleObject` | `0x18950` | 83 | UnwindData |  |
| 14 | `DllCanUnloadNow` | `0x18BE0` | 4,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `GetRoleTextW` | `0x19CA0` | 157 | UnwindData |  |
| 26 | `ObjectFromLresult` | `0x1A2C0` | 85 | UnwindData |  |
| 28 | `WindowFromAccessibleObject` | `0x1A6E0` | 53 | UnwindData |  |
| 21 | `GetStateTextW` | `0x1B540` | 67 | UnwindData |  |
| 1 | `DllRegisterServer` | `0x1EC10` | 176,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllUnregisterServer` | `0x1EC10` | 176,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `AccGetRunningUtilityState` | `0x49CB0` | 139 | UnwindData |  |
| 4 | `AccNotifyTouchInteraction` | `0x4A470` | 127 | UnwindData |  |
| 5 | `AccSetRunningUtilityState` | `0x4A500` | 65 | UnwindData |  |
| 8 | `AccessibleObjectFromPoint` | `0x4A550` | 67 | UnwindData |  |
| 12 | `CreateStdAccessibleProxyA` | `0x4A5A0` | 67 | UnwindData |  |
| 13 | `CreateStdAccessibleProxyW` | `0x4A5F0` | 67 | UnwindData |  |
| 16 | `GetOleaccVersionInfo` | `0x4A640` | 64 | UnwindData |  |
| 18 | `GetRoleTextA` | `0x4A690` | 72 | UnwindData |  |
| 20 | `GetStateTextA` | `0x4A6E0` | 72 | UnwindData |  |
| 22 | `IID_IAccessible` | `0x59888` | 1,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `IID_IAccessibleHandler` | `0x59ED0` | 5,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `LIBID_Accessibility` | `0x5B298` | 0 | Indeterminate |  |
