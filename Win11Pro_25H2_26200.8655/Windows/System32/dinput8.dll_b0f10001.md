# Binary Specification: dinput8.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dinput8.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b0f10001fccd05e9863d84588be9b9f8389656d95177287dd4c6cf3be4bf1dfe`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DirectInput8Create` | `0x111E0` | 622 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x1A540` | 167 | UnwindData |  |
| 6 | `GetdfDIJoystick` | `0x1D1D0` | 24,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x231B0` | 30,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x2A850` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x2AAD0` | 10,177 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
