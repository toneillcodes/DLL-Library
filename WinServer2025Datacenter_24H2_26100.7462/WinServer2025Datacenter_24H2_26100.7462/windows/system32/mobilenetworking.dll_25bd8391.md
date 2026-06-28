# Binary Specification: mobilenetworking.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mobilenetworking.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `25bd839143ea6ba4f1728fc0c937cbf5e35472c204817df80ca89a88cc6c7acf`
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
| 46 | `PersistentRegPathCreateKey` | `0x7200` | 45 | UnwindData |  |
| 42 | `NdisQueryMaxPayloadSizeByGuid` | `0x7360` | 89 | UnwindData |  |
| 25 | `GetPersistentRegPath` | `0x7650` | 434 | UnwindData |  |
| 43 | `NdisQueryPhysicalMedium` | `0x7880` | 120 | UnwindData |  |
| 16 | `DiffTimeInSec` | `0x7BF0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `StopTimer` | `0x7CA0` | 40 | UnwindData |  |
| 71 | `StartTimer` | `0x7E70` | 536 | UnwindData |  |
| 7 | `ConvertByteArrayToWideStr` | `0x80E0` | 190 | UnwindData |  |
| 9 | `CreateReadWriteLock` | `0x81E0` | 437 | UnwindData |  |
| 13 | `DeleteReadWriteLock` | `0x83A0` | 225 | UnwindData |  |
| 15 | `DiffTimeInMSec` | `0x8490` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `L2InitializeAuditing` | `0x8540` | 353 | UnwindData |  |
| 39 | `L2DeinitializeAuditing` | `0x8960` | 253 | UnwindData |  |
| 50 | `PersistentRegPathSetDWORD` | `0x8C90` | 49 | UnwindData |  |
| 38 | `IsWinPE` | `0x8DB0` | 98 | UnwindData |  |
| 36 | `InitializeTimers` | `0x8E20` | 315 | UnwindData |  |
| 63 | `ReleaseReadLock` | `0x8F70` | 144 | UnwindData |  |
| 35 | `InitSecUtils` | `0x9010` | 401 | UnwindData |  |
| 5 | `BindNetworkInterfaceIdToAccountId` | `0x9220` | 769 | UnwindData |  |
| 37 | `IsDomainMemberMode` | `0x9530` | 89 | UnwindData |  |
| 26 | `GetPersistentRegPathFromRegPath` | `0xB570` | 203 | UnwindData |  |
| 47 | `PersistentRegPathGetDWORD` | `0xB720` | 260 | UnwindData |  |
| 48 | `PersistentRegPathGetValue` | `0xB830` | 262 | UnwindData |  |
| 51 | `PersistentRegPathSetString` | `0xB940` | 104 | UnwindData |  |
| 52 | `PersistentRegPathSetValue` | `0xB9B0` | 245 | UnwindData |  |
| 1 | `AcquireReadLock` | `0xBAB0` | 172 | UnwindData |  |
| 66 | `ReplaceObjectWithPersistedSettings` | `0xC420` | 472 | UnwindData |  |
| 11 | `DeInitializeTimers` | `0xC670` | 306 | UnwindData |  |
| 19 | `GetAdapterConnectivity` | `0xCB90` | 375 | UnwindData |  |
| 41 | `LogBailError` | `0xCFC0` | 63 | UnwindData |  |
| 73 | `TraceAssert` | `0xD010` | 57 | UnwindData |  |
| 79 | `WmiEnumerateAdapters` | `0xD1E0` | 257 | UnwindData |  |
| 80 | `WmiQueryMediaSupported` | `0xD420` | 235 | UnwindData |  |
| 81 | `WmiQueryPhysicalMedium` | `0xD520` | 122 | UnwindData |  |
| 53 | `RaCheckRpcAllowed` | `0xD6A0` | 802 | UnwindData |  |
| 56 | `RaFreeSidList` | `0xD9D0` | 138 | UnwindData |  |
| 57 | `RaFreeTokenUserInfo` | `0xDA60` | 108 | UnwindData |  |
| 58 | `RaGetTokenUserInfo` | `0xDAE0` | 457 | UnwindData |  |
| 59 | `RaInitSidList` | `0xDCB0` | 457 | UnwindData |  |
| 60 | `RaQueryRpcClientToken` | `0xDE80` | 276 | UnwindData |  |
| 20 | `GetMnoSmsBindingDeviceInterfacePath` | `0xE300` | 105 | UnwindData |  |
| 21 | `GetNetworkAccountBindingDeviceInterfacePath` | `0xE370` | 106 | UnwindData |  |
| 24 | `GetOemIhvSmsBindingDeviceInterfacePath` | `0xE3E0` | 429 | UnwindData |  |
| 44 | `NetworkAccountBindingAccessCheck` | `0xEEC0` | 769 | UnwindData |  |
| 45 | `NetworkAccountBindingAccessCheckByInterfaceId` | `0xF1D0` | 297 | UnwindData |  |
| 68 | `SetMnoSmsBindingDeviceInterfacePath` | `0xF560` | 90 | UnwindData |  |
| 69 | `SetNetworkAccountBindingDeviceInterfacePath` | `0xF5C0` | 89 | UnwindData |  |
| 70 | `SetOemIhvSmsBindingDeviceInterfacePath` | `0xF620` | 538 | UnwindData |  |
| 74 | `UnbindNetworkInterfaceId` | `0xF9F0` | 415 | UnwindData |  |
