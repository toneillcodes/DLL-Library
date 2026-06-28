# Binary Specification: ProximityServicePal.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ProximityServicePal.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `42ee9eaa3b885db695dd6286ab6b43483a41944d013eea859f00a418a39d886e`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `PAL_RegisterConsoleDisplayStateNotifications` | `0x13F0` | 462 | UnwindData |  |
| 15 | `PAL_GetConsoleSessionInfo` | `0x15D0` | 732 | UnwindData |  |
| 17 | `PAL_IsCallerAssignedAccessUser` | `0x1F50` | 6 | UnwindData |  |
| 2 | `PAL_BluetoothEnableDiscovery` | `0x4360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PAL_BluetoothFindDeviceClose` | `0x4360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PAL_BluetoothFindFirstDevice` | `0x4360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `PAL_BluetoothFindRadioClose` | `0x4360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `PAL_ServiceFreeTransientObjectSecurityAttribute` | `0x4360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `PAL_HasWFDHardwareSupport` | `0x4370` | 1,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `PAL_FWResetIndicatedTupleInUse` | `0x4AB0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `PAL_UnregisterConsoleDisplayStateNotifications` | `0x4D20` | 43 | UnwindData |  |
| 1 | `PAL_AllowNetworkInterface` | `0xE570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PAL_BluetoothFindFirstRadio` | `0xE590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `PAL_ServiceQueryTransientObjectSecurityAttribute` | `0xE590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `PAL_BluetoothOpenFirewall` | `0xE5A0` | 389 | UnwindData |  |
| 8 | `PAL_ConvertAppIdToPackageName` | `0xE730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PAL_CreateForegroundNotifier` | `0xE740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `PAL_CreateUnicastIpAddressEntry` | `0xE750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `PAL_DeleteUnicastIpAddressEntry` | `0xE770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `PAL_FWIndicateTupleInUse` | `0xE790` | 99 | UnwindData |  |
| 14 | `PAL_GetCallingApplicationInfo` | `0xE800` | 872 | UnwindData |  |
| 18 | `PAL_IsInteractiveApplicationId` | `0xEB70` | 667 | UnwindData |  |
| 19 | `PAL_IsMachineDomainJoined` | `0xEE20` | 380 | UnwindData |  |
| 20 | `PAL_OpenProcessForQuery` | `0xEFB0` | 78 | UnwindData |  |
| 21 | `PAL_RegisterConnectedStandbyNotification` | `0xF010` | 398 | UnwindData |  |
| 25 | `PAL_UnregisterConnectedStandbyNotification` | `0xF1B0` | 341 | UnwindData |  |
| 27 | `PAL_VerifyCallerIsElevated` | `0xF310` | 149 | UnwindData |  |
| 28 | `PAL_CoCreateInstanceInSession` | `0x10340` | 1,659 | UnwindData |  |
