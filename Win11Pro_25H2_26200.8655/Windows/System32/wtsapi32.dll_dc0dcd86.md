# Binary Specification: wtsapi32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wtsapi32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dc0dcd86ea95d5f492883bb2cb5f15698060da5ab979dfdea26c0bd41fb7ef00`
* **Total Exported Functions:** 76

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `QueryUserToken` | `0x1930` | 507 | UnwindData |  |
| 49 | `WTSQueryUserToken` | `0x1930` | 507 | UnwindData |  |
| 21 | `WTSEnumerateProcessesA` | `0x1B40` | 918 | UnwindData |  |
| 24 | `WTSEnumerateProcessesW` | `0x1EE0` | 748 | UnwindData |  |
| 22 | `WTSEnumerateProcessesExA` | `0x22A0` | 176 | UnwindData |  |
| 23 | `WTSEnumerateProcessesExW` | `0x2600` | 24 | UnwindData |  |
| 45 | `WTSQuerySessionInformationA` | `0x2A00` | 529 | UnwindData |  |
| 46 | `WTSQuerySessionInformationW` | `0x2C20` | 2,956 | UnwindData |  |
| 33 | `WTSFreeMemoryExW` | `0x3940` | 38 | UnwindData |  |
| 30 | `WTSEnumerateSessionsW` | `0x3AA0` | 278 | UnwindData |  |
| 29 | `WTSEnumerateSessionsExW` | `0x3D00` | 10 | UnwindData |  |
| 27 | `WTSEnumerateSessionsA` | `0x49A0` | 829 | UnwindData |  |
| 31 | `WTSFreeMemory` | `0x4E30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `WTSRegisterSessionNotification` | `0x4E50` | 152 | UnwindData |  |
| 66 | `WTSUnRegisterSessionNotification` | `0x4F40` | 128 | UnwindData |  |
| 2 | `QueryActiveSession` | `0x4FD0` | 29 | UnwindData |  |
| 4 | `RegisterUsertokenForNoWinlogon` | `0x4FD0` | 29 | UnwindData |  |
| 60 | `WTSSetUserConfigW` | `0x5000` | 37 | UnwindData |  |
| 1 | `IsInteractiveUserSession` | `0x54B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `WTSWaitSystemEvent` | `0x54C0` | 334 | UnwindData |  |
| 51 | `WTSRegisterSessionNotificationEx` | `0x5620` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `WTSUnRegisterSessionNotificationEx` | `0x56E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `WTSVirtualChannelOpenEx` | `0x5700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `WTSVirtualChannelQuery` | `0x5720` | 355 | UnwindData |  |
| 68 | `WTSVirtualChannelClose` | `0x5890` | 61 | UnwindData |  |
| 44 | `WTSQueryListenerConfigW` | `0x5930` | 749 | UnwindData |  |
| 6 | `WTSCloseServer` | `0x5C30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `WTSOpenServerExW` | `0x5C50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `WTSOpenServerA` | `0x5C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `WTSOpenServerW` | `0x5C90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `WTSQueryUserConfigW` | `0x5CB0` | 36 | UnwindData |  |
| 14 | `WTSConnectSessionW` | `0x6120` | 40 | UnwindData |  |
| 32 | `WTSFreeMemoryExA` | `0x63A0` | 65 | UnwindData |  |
| 69 | `WTSVirtualChannelOpen` | `0x63F0` | 5,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `WTSConnectSessionA` | `0x7850` | 249 | UnwindData |  |
| 18 | `WTSEnableChildSessions` | `0x7950` | 25 | UnwindData |  |
| 34 | `WTSGetChildSessionId` | `0x7970` | 54 | UnwindData |  |
| 37 | `WTSIsChildSessionsEnabled` | `0x79B0` | 56 | UnwindData |  |
| 56 | `WTSSetRenderHint` | `0x79F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `WTSShutdownSystem` | `0x7A10` | 201 | UnwindData |  |
| 62 | `WTSStartRemoteControlSessionA` | `0x7AE0` | 236 | UnwindData |  |
| 63 | `WTSStartRemoteControlSessionW` | `0x7BE0` | 42 | UnwindData |  |
| 64 | `WTSStopRemoteControlSession` | `0x7C10` | 32 | UnwindData |  |
| 25 | `WTSEnumerateServersA` | `0x7DC0` | 417 | UnwindData |  |
| 26 | `WTSEnumerateServersW` | `0x7F70` | 400 | UnwindData |  |
| 40 | `WTSOpenServerExA` | `0x8110` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WTSActiveSessionExists` | `0x8590` | 25 | UnwindData |  |
| 17 | `WTSDisconnectSession` | `0x85B0` | 25 | UnwindData |  |
| 28 | `WTSEnumerateSessionsExA` | `0x85D0` | 483 | UnwindData |  |
| 38 | `WTSLogoffSession` | `0x87C0` | 25 | UnwindData |  |
| 52 | `WTSSendMessageA` | `0x87E0` | 135 | UnwindData |  |
| 53 | `WTSSendMessageW` | `0x8870` | 135 | UnwindData |  |
| 57 | `WTSSetSessionInformationA` | `0x8900` | 3,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `WTSSetSessionInformationW` | `0x8900` | 3,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `WTSTerminateProcess` | `0x94D0` | 25 | UnwindData |  |
| 71 | `WTSVirtualChannelPurgeInput` | `0x95C0` | 20 | UnwindData |  |
| 72 | `WTSVirtualChannelPurgeOutput` | `0x95E0` | 20 | UnwindData |  |
| 74 | `WTSVirtualChannelRead` | `0x9600` | 271 | UnwindData |  |
| 75 | `WTSVirtualChannelWrite` | `0x9720` | 172 | UnwindData |  |
| 47 | `WTSQueryUserConfigA` | `0x9E60` | 530 | UnwindData |  |
| 59 | `WTSSetUserConfigA` | `0xA080` | 476 | UnwindData |  |
| 15 | `WTSCreateListenerA` | `0xA5B0` | 276 | UnwindData |  |
| 16 | `WTSCreateListenerW` | `0xA6D0` | 2,007 | UnwindData |  |
| 19 | `WTSEnumerateListenersA` | `0xAEB0` | 305 | UnwindData |  |
| 20 | `WTSEnumerateListenersW` | `0xAFF0` | 404 | UnwindData |  |
| 35 | `WTSGetListenerSecurityA` | `0xB190` | 227 | UnwindData |  |
| 36 | `WTSGetListenerSecurityW` | `0xB280` | 602 | UnwindData |  |
| 43 | `WTSQueryListenerConfigA` | `0xB4E0` | 307 | UnwindData |  |
| 54 | `WTSSetListenerSecurityA` | `0xB620` | 200 | UnwindData |  |
| 55 | `WTSSetListenerSecurityW` | `0xB6F0` | 435 | UnwindData |  |
| 7 | `WTSCloudAuthClose` | `0x12840` | 49 | UnwindData |  |
| 8 | `WTSCloudAuthConvertAssertionToSerializedUserCredential` | `0x12880` | 101 | UnwindData |  |
| 9 | `WTSCloudAuthDuplicateSerializedUserCredential` | `0x128F0` | 117 | UnwindData |  |
| 10 | `WTSCloudAuthGetServerNonce` | `0x12970` | 64 | UnwindData |  |
| 11 | `WTSCloudAuthNetworkLogonWithSerializedCredential` | `0x129C0` | 76 | UnwindData |  |
| 12 | `WTSCloudAuthOpen` | `0x12A20` | 59 | UnwindData |  |
