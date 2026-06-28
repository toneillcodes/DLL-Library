# Binary Specification: oleacc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\oleacc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `40d73e20a9f008aa05ac0d57c31f8513d01f21b8070ac201124a8afa8f82586c`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 17 | `GetProcessHandleFromHwnd` | `0x46B0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `DllGetClassObject` | `0x4850` | 396 | UnwindData |  |
| 10 | `AccessibleObjectFromWindowTimeout` | `0x4DF0` | 3,140 | UnwindData |  |
| 7 | `AccessibleObjectFromEvent` | `0x6FA0` | 430 | UnwindData |  |
| 27 | `PropMgrClient_LookupProp` | `0xC2F0` | 143 | UnwindData |  |
| 9 | `AccessibleObjectFromWindow` | `0xFAD0` | 67 | UnwindData |  |
| 25 | `LresultFromObject` | `0x12F50` | 62 | UnwindData |  |
| 6 | `AccessibleChildren` | `0x14880` | 40 | UnwindData |  |
| 11 | `CreateStdAccessibleObject` | `0x189A0` | 83 | UnwindData |  |
| 14 | `DllCanUnloadNow` | `0x18C30` | 4,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `GetRoleTextW` | `0x19CF0` | 157 | UnwindData |  |
| 26 | `ObjectFromLresult` | `0x1A310` | 85 | UnwindData |  |
| 28 | `WindowFromAccessibleObject` | `0x1A730` | 53 | UnwindData |  |
| 21 | `GetStateTextW` | `0x1B590` | 67 | UnwindData |  |
| 1 | `DllRegisterServer` | `0x1EC60` | 188,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllUnregisterServer` | `0x1EC60` | 188,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `AccGetRunningUtilityState` | `0x4CB00` | 139 | UnwindData |  |
| 4 | `AccNotifyTouchInteraction` | `0x4D2C0` | 127 | UnwindData |  |
| 5 | `AccSetRunningUtilityState` | `0x4D350` | 65 | UnwindData |  |
| 8 | `AccessibleObjectFromPoint` | `0x4D3A0` | 67 | UnwindData |  |
| 12 | `CreateStdAccessibleProxyA` | `0x4D3F0` | 67 | UnwindData |  |
| 13 | `CreateStdAccessibleProxyW` | `0x4D440` | 67 | UnwindData |  |
| 16 | `GetOleaccVersionInfo` | `0x4D490` | 64 | UnwindData |  |
| 18 | `GetRoleTextA` | `0x4D4E0` | 72 | UnwindData |  |
| 20 | `GetStateTextA` | `0x4D530` | 72 | UnwindData |  |
| 22 | `IID_IAccessible` | `0x5C8C8` | 1,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `IID_IAccessibleHandler` | `0x5CF10` | 5,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `LIBID_Accessibility` | `0x5E2D8` | 0 | Indeterminate |  |
