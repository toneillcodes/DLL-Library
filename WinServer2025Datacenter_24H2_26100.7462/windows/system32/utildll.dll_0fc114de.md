# Binary Specification: utildll.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\utildll.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0fc114defa66d2e83c4589b1f615b780248d7d6359ad40be6a88ff01d68fb7e5`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 34 | `WinEnumerateDevices` | `0x1010` | 319 | UnwindData |  |
| 25 | `RegGetNetworkDeviceName` | `0x1160` | 1,711 | UnwindData |  |
| 29 | `StrConnectState` | `0x1820` | 340 | UnwindData |  |
| 2 | `CachedGetUserFromSid` | `0x1CA0` | 57 | UnwindData |  |
| 1 | `AsyncDeviceEnumerate` | `0x2D30` | 899 | UnwindData |  |
| 3 | `CalculateDiffTime` | `0x30C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `CalculateElapsedTime` | `0x30E0` | 271 | UnwindData |  |
| 5 | `CompareElapsedTime` | `0x3410` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ConfigureModem` | `0x3460` | 402 | UnwindData |  |
| 7 | `CurrentDateTimeString` | `0x3600` | 467 | UnwindData |  |
| 8 | `DateTimeString` | `0x37E0` | 540 | UnwindData |  |
| 9 | `ElapsedTimeString` | `0x3A20` | 265 | UnwindData |  |
| 10 | `EnumerateMultiUserServers` | `0x3B30` | 351 | UnwindData |  |
| 11 | `FormDecoratedAsyncDeviceName` | `0x4310` | 54 | UnwindData |  |
| 12 | `GetAssociatedPortName` | `0x4350` | 268 | UnwindData |  |
| 13 | `GetSystemMessageA` | `0x4470` | 171 | UnwindData |  |
| 14 | `GetSystemMessageW` | `0x4530` | 575 | UnwindData |  |
| 15 | `GetUnknownString` | `0x4780` | 78 | UnwindData |  |
| 16 | `GetUserFromSid` | `0x47E0` | 519 | UnwindData |  |
| 17 | `HaveAnonymousUsersChanged` | `0x49F0` | 271 | UnwindData |  |
| 18 | `InitializeAnonymousUserCompareList` | `0x4B10` | 72 | UnwindData |  |
| 19 | `InstallModem` | `0x4B60` | 302 | UnwindData |  |
| 20 | `IsPartOfDomain` | `0x4CA0` | 182 | UnwindData |  |
| 21 | `NetBIOSDeviceEnumerate` | `0x4D60` | 218 | UnwindData |  |
| 22 | `NetworkDeviceEnumerate` | `0x50D0` | 587 | UnwindData |  |
| 23 | `ParseDecoratedAsyncDeviceName` | `0x5330` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `QueryCurrentWinStation` | `0x53E0` | 322 | UnwindData |  |
| 26 | `RegGetNetworkServiceName` | `0x5530` | 1,160 | UnwindData |  |
| 27 | `StandardErrorMessage` | `0x59C0` | 799 | UnwindData |  |
| 28 | `StrAsyncConnectState` | `0x5CF0` | 100 | UnwindData |  |
| 30 | `StrProcessState` | `0x5D60` | 114 | UnwindData |  |
| 31 | `StrSdClass` | `0x5DE0` | 195 | UnwindData |  |
| 32 | `StrSystemWaitReason` | `0x5EB0` | 114 | UnwindData |  |
| 33 | `TestUserForAdmin` | `0x60D0` | 204 | UnwindData |  |
