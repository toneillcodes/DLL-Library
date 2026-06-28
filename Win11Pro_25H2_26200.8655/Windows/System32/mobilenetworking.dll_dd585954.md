# Binary Specification: mobilenetworking.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mobilenetworking.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dd5859541aa51315a83b8f448c5f75822e84a8907ff8529c5c34fa2c05d8ec2e`
* **Total Exported Functions:** 81

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 77 | `VerifyRpcClientAccess` | `0x1130` | 675 | UnwindData |  |
| 78 | `VerifyRpcClientAccessToSecurityDescriptor` | `0x13E0` | 1,264 | UnwindData |  |
| 34 | `HtReferenceHandleWithTag` | `0x1D30` | 230 | UnwindData |  |
| 65 | `ReplaceObject` | `0x1E20` | 8 | UnwindData |  |
| 62 | `RegisterUserType` | `0x20D0` | 6 | UnwindData |  |
| 61 | `RegisterObject` | `0x2260` | 666 | UnwindData |  |
| 6 | `CheckRpcClientTokenMembership` | `0x2500` | 460 | UnwindData |  |
| 27 | `GetSDDetailsFromObjectID` | `0x26E0` | 8 | UnwindData |  |
| 8 | `ConvertSDDLToValidSecurityDescriptor` | `0x3080` | 642 | UnwindData |  |
| 76 | `ValidateSecurityDescriptor` | `0x3310` | 74 | UnwindData |  |
| 67 | `SetBufferAndLength` | `0x3660` | 503 | UnwindData |  |
| 3 | `AllocateAndCopyPointerData` | `0x3860` | 257 | UnwindData |  |
| 10 | `CreateTimer` | `0x3970` | 7 | UnwindData |  |
| 14 | `DeleteTimer` | `0x3C40` | 460 | UnwindData |  |
| 18 | `FreeSecurityDescriptor` | `0x3E20` | 46 | UnwindData |  |
| 55 | `RaDestroySid` | `0x3FE0` | 13 | UnwindData |  |
| 54 | `RaCreateWellKnownSid` | `0x4120` | 1,573 | UnwindData |  |
| 29 | `HtCreateHandleTable` | `0x4750` | 78 | UnwindData |  |
| 4 | `AllocateMemory` | `0x4890` | 327 | UnwindData |  |
| 32 | `HtNewHandle` | `0x49E0` | 65 | UnwindData |  |
| 31 | `HtDestroyHandleTable` | `0x4C30` | 59 | UnwindData |  |
| 17 | `FreeMemory` | `0x4D60` | 41 | UnwindData |  |
| 12 | `DeinitSecUtils` | `0x51D0` | 126 | UnwindData |  |
| 30 | `HtDereferenceHandleWithTag` | `0x5360` | 253 | UnwindData |  |
| 2 | `AcquireWriteLock` | `0x5700` | 379 | UnwindData |  |
| 64 | `ReleaseWriteLock` | `0x5890` | 273 | UnwindData |  |
| 33 | `HtPeekReferenceCountOnHandle` | `0x59B0` | 146 | UnwindData |  |
| 28 | `GetSystemTimeAsUlongLong` | `0x5AF0` | 29 | UnwindData |  |
| 23 | `GetNetworkInterfaceIdBoundToAccountId` | `0x5B20` | 90 | UnwindData |  |
| 75 | `ValidateNetworkAccountIdBinding` | `0x6020` | 546 | UnwindData |  |
| 22 | `GetNetworkAccountIdBoundToInterfaceId` | `0x6250` | 96 | UnwindData |  |
| 49 | `PersistentRegPathOpenKey` | `0x70E0` | 56 | UnwindData |  |
| 46 | `PersistentRegPathCreateKey` | `0x7220` | 45 | UnwindData |  |
| 42 | `NdisQueryMaxPayloadSizeByGuid` | `0x73A0` | 89 | UnwindData |  |
| 25 | `GetPersistentRegPath` | `0x7690` | 434 | UnwindData |  |
| 43 | `NdisQueryPhysicalMedium` | `0x78C0` | 120 | UnwindData |  |
| 16 | `DiffTimeInSec` | `0x7C30` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `StopTimer` | `0x7CE0` | 40 | UnwindData |  |
| 71 | `StartTimer` | `0x7EB0` | 536 | UnwindData |  |
| 7 | `ConvertByteArrayToWideStr` | `0x8120` | 190 | UnwindData |  |
| 9 | `CreateReadWriteLock` | `0x8220` | 437 | UnwindData |  |
| 13 | `DeleteReadWriteLock` | `0x83E0` | 225 | UnwindData |  |
| 15 | `DiffTimeInMSec` | `0x84D0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `L2InitializeAuditing` | `0x8580` | 353 | UnwindData |  |
| 39 | `L2DeinitializeAuditing` | `0x89A0` | 253 | UnwindData |  |
| 50 | `PersistentRegPathSetDWORD` | `0x8CD0` | 49 | UnwindData |  |
| 38 | `IsWinPE` | `0x8E10` | 98 | UnwindData |  |
| 36 | `InitializeTimers` | `0x8E80` | 315 | UnwindData |  |
| 63 | `ReleaseReadLock` | `0x8FD0` | 144 | UnwindData |  |
| 35 | `InitSecUtils` | `0x9070` | 401 | UnwindData |  |
| 5 | `BindNetworkInterfaceIdToAccountId` | `0x9280` | 769 | UnwindData |  |
| 37 | `IsDomainMemberMode` | `0x9590` | 89 | UnwindData |  |
| 26 | `GetPersistentRegPathFromRegPath` | `0xB5D0` | 203 | UnwindData |  |
| 47 | `PersistentRegPathGetDWORD` | `0xB780` | 288 | UnwindData |  |
| 48 | `PersistentRegPathGetValue` | `0xB8B0` | 290 | UnwindData |  |
| 51 | `PersistentRegPathSetString` | `0xB9E0` | 104 | UnwindData |  |
| 52 | `PersistentRegPathSetValue` | `0xBA50` | 273 | UnwindData |  |
| 1 | `AcquireReadLock` | `0xBB70` | 172 | UnwindData |  |
| 66 | `ReplaceObjectWithPersistedSettings` | `0xC4E0` | 472 | UnwindData |  |
| 11 | `DeInitializeTimers` | `0xC730` | 306 | UnwindData |  |
| 19 | `GetAdapterConnectivity` | `0xCC50` | 375 | UnwindData |  |
| 41 | `LogBailError` | `0xD080` | 63 | UnwindData |  |
| 73 | `TraceAssert` | `0xD0D0` | 57 | UnwindData |  |
| 79 | `WmiEnumerateAdapters` | `0xD2A0` | 257 | UnwindData |  |
| 80 | `WmiQueryMediaSupported` | `0xD4E0` | 235 | UnwindData |  |
| 81 | `WmiQueryPhysicalMedium` | `0xD5E0` | 122 | UnwindData |  |
| 53 | `RaCheckRpcAllowed` | `0xD760` | 802 | UnwindData |  |
| 56 | `RaFreeSidList` | `0xDA90` | 138 | UnwindData |  |
| 57 | `RaFreeTokenUserInfo` | `0xDB20` | 108 | UnwindData |  |
| 58 | `RaGetTokenUserInfo` | `0xDBA0` | 457 | UnwindData |  |
| 59 | `RaInitSidList` | `0xDD70` | 457 | UnwindData |  |
| 60 | `RaQueryRpcClientToken` | `0xDF40` | 276 | UnwindData |  |
| 20 | `GetMnoSmsBindingDeviceInterfacePath` | `0xE3C0` | 105 | UnwindData |  |
| 21 | `GetNetworkAccountBindingDeviceInterfacePath` | `0xE430` | 106 | UnwindData |  |
| 24 | `GetOemIhvSmsBindingDeviceInterfacePath` | `0xE4A0` | 429 | UnwindData |  |
| 44 | `NetworkAccountBindingAccessCheck` | `0xEF80` | 769 | UnwindData |  |
| 45 | `NetworkAccountBindingAccessCheckByInterfaceId` | `0xF290` | 297 | UnwindData |  |
| 68 | `SetMnoSmsBindingDeviceInterfacePath` | `0xF620` | 90 | UnwindData |  |
| 69 | `SetNetworkAccountBindingDeviceInterfacePath` | `0xF680` | 89 | UnwindData |  |
| 70 | `SetOemIhvSmsBindingDeviceInterfacePath` | `0xF6E0` | 538 | UnwindData |  |
| 74 | `UnbindNetworkInterfaceId` | `0xFAB0` | 415 | UnwindData |  |
