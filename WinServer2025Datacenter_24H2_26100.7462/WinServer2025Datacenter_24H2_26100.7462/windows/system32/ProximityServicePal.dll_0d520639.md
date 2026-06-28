# Binary Specification: ProximityServicePal.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ProximityServicePal.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0d5206399acef5b65f73dd4ca1de1a8f5e470930a13053b64c5e7a2e2fece1e1`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `PAL_RegisterConsoleDisplayStateNotifications` | `0x13E0` | 462 | UnwindData |  |
| 15 | `PAL_GetConsoleSessionInfo` | `0x15C0` | 732 | UnwindData |  |
| 17 | `PAL_IsCallerAssignedAccessUser` | `0x1F40` | 6 | UnwindData |  |
| 2 | `PAL_BluetoothEnableDiscovery` | `0x4350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PAL_BluetoothFindDeviceClose` | `0x4350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `PAL_BluetoothFindFirstDevice` | `0x4350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `PAL_BluetoothFindRadioClose` | `0x4350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `PAL_ServiceFreeTransientObjectSecurityAttribute` | `0x4350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `PAL_HasWFDHardwareSupport` | `0x4360` | 1,856 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `PAL_FWResetIndicatedTupleInUse` | `0x4AA0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `PAL_UnregisterConsoleDisplayStateNotifications` | `0x4D10` | 43 | UnwindData |  |
| 1 | `PAL_AllowNetworkInterface` | `0xDED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PAL_BluetoothFindFirstRadio` | `0xDEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `PAL_ServiceQueryTransientObjectSecurityAttribute` | `0xDEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `PAL_BluetoothOpenFirewall` | `0xDF00` | 389 | UnwindData |  |
| 8 | `PAL_ConvertAppIdToPackageName` | `0xE090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PAL_CreateForegroundNotifier` | `0xE0A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `PAL_CreateUnicastIpAddressEntry` | `0xE0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `PAL_DeleteUnicastIpAddressEntry` | `0xE0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `PAL_FWIndicateTupleInUse` | `0xE0F0` | 99 | UnwindData |  |
| 14 | `PAL_GetCallingApplicationInfo` | `0xE160` | 872 | UnwindData |  |
| 18 | `PAL_IsInteractiveApplicationId` | `0xE4D0` | 667 | UnwindData |  |
| 19 | `PAL_IsMachineDomainJoined` | `0xE780` | 380 | UnwindData |  |
| 20 | `PAL_OpenProcessForQuery` | `0xE910` | 78 | UnwindData |  |
| 21 | `PAL_RegisterConnectedStandbyNotification` | `0xE970` | 398 | UnwindData |  |
| 25 | `PAL_UnregisterConnectedStandbyNotification` | `0xEB10` | 341 | UnwindData |  |
| 27 | `PAL_VerifyCallerIsElevated` | `0xEC70` | 149 | UnwindData |  |
| 28 | `PAL_CoCreateInstanceInSession` | `0x10140` | 1,659 | UnwindData |  |
