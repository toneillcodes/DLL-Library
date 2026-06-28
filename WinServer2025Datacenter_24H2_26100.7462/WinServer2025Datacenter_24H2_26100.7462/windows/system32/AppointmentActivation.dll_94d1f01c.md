# Binary Specification: AppointmentActivation.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AppointmentActivation.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `94d1f01c6e7ffe8dbc99e374748b30fb4672b85e86eade163d5d84b5861eb447`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllCanUnloadNow` | `0x1190` | 407 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x1CD0` | 165 | UnwindData |  |
| 12 | `GetProxyDllInfo` | `0x4360` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllGetActivationFactory` | `0x4550` | 45 | UnwindData |  |
| 1 | `SerializeAppointmentIdsResult` | `0x4810` | 393 | UnwindData |  |
| 2 | `SerializeCalendarIdResult` | `0x49A0` | 292 | UnwindData |  |
| 3 | `AwaitAppointmentActivation` | `0x8950` | 722 | UnwindData |  |
| 9 | `GetAddAppointmentArgument` | `0x8C30` | 558 | UnwindData |  |
| 10 | `GetCalendarChooserArgument` | `0x8E70` | 937 | UnwindData |  |
| 13 | `GetRemoveAppointmentArgument` | `0x9220` | 733 | UnwindData |  |
| 14 | `GetReplaceAppointmentArgument` | `0x9510` | 856 | UnwindData |  |
| 17 | `ShowAddAppointment` | `0x9870` | 219 | UnwindData |  |
| 18 | `ShowAddAppointmentAsync` | `0x9960` | 176 | UnwindData |  |
| 19 | `ShowAppointmentDetails` | `0x9A20` | 831 | UnwindData |  |
| 20 | `ShowCalendarChooser` | `0x9D70` | 209 | UnwindData |  |
| 21 | `ShowCalendarChooserAsync` | `0x9E50` | 162 | UnwindData |  |
| 22 | `ShowRemoveAppointment` | `0x9F00` | 227 | UnwindData |  |
| 23 | `ShowRemoveAppointmentAsync` | `0x9FF0` | 195 | UnwindData |  |
| 24 | `ShowReplaceAppointment` | `0xA0C0` | 240 | UnwindData |  |
| 25 | `ShowReplaceAppointmentAsync` | `0xA1C0` | 205 | UnwindData |  |
| 26 | `ShowTimeFrame` | `0xA2A0` | 617 | UnwindData |  |
| 4 | `DeserializeActivationArgs` | `0xBE40` | 1,371 | UnwindData |  |
| 5 | `DeserializeAppointment` | `0xC3B0` | 537 | UnwindData |  |
| 16 | `ReleaseActivationArgs` | `0xC5D0` | 22 | UnwindData |  |
| 11 | `GetLegacyAppointmentDetailsArgumentString` | `0xDC50` | 505 | UnwindData |  |
| 15 | `GetWindowIdOfHost` | `0xE1C0` | 68 | UnwindData |  |
