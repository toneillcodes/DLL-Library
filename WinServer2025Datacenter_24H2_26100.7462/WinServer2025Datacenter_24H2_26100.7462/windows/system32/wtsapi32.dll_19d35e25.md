# Binary Specification: wtsapi32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wtsapi32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `19d35e25e3ce431b7ca6b25cb60f19dff9ffbede098bc7762baadf4f6220974b`
* **Total Exported Functions:** 76

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `QueryUserToken` | `0x1770` | 507 | UnwindData |  |
| 49 | `WTSQueryUserToken` | `0x1770` | 507 | UnwindData |  |
| 21 | `WTSEnumerateProcessesA` | `0x1980` | 918 | UnwindData |  |
| 24 | `WTSEnumerateProcessesW` | `0x1D20` | 748 | UnwindData |  |
| 22 | `WTSEnumerateProcessesExA` | `0x20E0` | 176 | UnwindData |  |
| 23 | `WTSEnumerateProcessesExW` | `0x2440` | 24 | UnwindData |  |
| 45 | `WTSQuerySessionInformationA` | `0x2840` | 529 | UnwindData |  |
| 46 | `WTSQuerySessionInformationW` | `0x2A60` | 3,208 | UnwindData |  |
| 33 | `WTSFreeMemoryExW` | `0x3870` | 50 | UnwindData |  |
| 30 | `WTSEnumerateSessionsW` | `0x39D0` | 278 | UnwindData |  |
| 29 | `WTSEnumerateSessionsExW` | `0x3C30` | 10 | UnwindData |  |
| 27 | `WTSEnumerateSessionsA` | `0x48D0` | 829 | UnwindData |  |
| 31 | `WTSFreeMemory` | `0x4D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `WTSRegisterSessionNotification` | `0x4D80` | 152 | UnwindData |  |
| 66 | `WTSUnRegisterSessionNotification` | `0x4E70` | 128 | UnwindData |  |
| 2 | `QueryActiveSession` | `0x4F00` | 29 | UnwindData |  |
| 4 | `RegisterUsertokenForNoWinlogon` | `0x4F00` | 29 | UnwindData |  |
| 60 | `WTSSetUserConfigW` | `0x4F30` | 37 | UnwindData |  |
| 1 | `IsInteractiveUserSession` | `0x53E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `WTSWaitSystemEvent` | `0x53F0` | 334 | UnwindData |  |
| 51 | `WTSRegisterSessionNotificationEx` | `0x5550` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `WTSUnRegisterSessionNotificationEx` | `0x5610` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `WTSVirtualChannelOpenEx` | `0x5630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `WTSVirtualChannelQuery` | `0x5650` | 355 | UnwindData |  |
| 68 | `WTSVirtualChannelClose` | `0x57C0` | 61 | UnwindData |  |
| 44 | `WTSQueryListenerConfigW` | `0x5860` | 749 | UnwindData |  |
| 6 | `WTSCloseServer` | `0x5B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `WTSOpenServerExW` | `0x5B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `WTSOpenServerA` | `0x5BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `WTSOpenServerW` | `0x5BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `WTSQueryUserConfigW` | `0x5BE0` | 36 | UnwindData |  |
| 14 | `WTSConnectSessionW` | `0x6050` | 40 | UnwindData |  |
| 32 | `WTSFreeMemoryExA` | `0x62D0` | 123 | UnwindData |  |
| 69 | `WTSVirtualChannelOpen` | `0x6360` | 5,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `WTSConnectSessionA` | `0x77D0` | 249 | UnwindData |  |
| 18 | `WTSEnableChildSessions` | `0x78D0` | 25 | UnwindData |  |
| 34 | `WTSGetChildSessionId` | `0x78F0` | 54 | UnwindData |  |
| 37 | `WTSIsChildSessionsEnabled` | `0x7930` | 56 | UnwindData |  |
| 56 | `WTSSetRenderHint` | `0x7970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `WTSShutdownSystem` | `0x7990` | 201 | UnwindData |  |
| 62 | `WTSStartRemoteControlSessionA` | `0x7A60` | 236 | UnwindData |  |
| 63 | `WTSStartRemoteControlSessionW` | `0x7B60` | 42 | UnwindData |  |
| 64 | `WTSStopRemoteControlSession` | `0x7B90` | 32 | UnwindData |  |
| 25 | `WTSEnumerateServersA` | `0x8750` | 417 | UnwindData |  |
| 26 | `WTSEnumerateServersW` | `0x8900` | 400 | UnwindData |  |
| 40 | `WTSOpenServerExA` | `0x8AA0` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `WTSActiveSessionExists` | `0x8FB0` | 25 | UnwindData |  |
| 17 | `WTSDisconnectSession` | `0x8FD0` | 25 | UnwindData |  |
| 28 | `WTSEnumerateSessionsExA` | `0x8FF0` | 483 | UnwindData |  |
| 38 | `WTSLogoffSession` | `0x91E0` | 25 | UnwindData |  |
| 52 | `WTSSendMessageA` | `0x9200` | 135 | UnwindData |  |
| 53 | `WTSSendMessageW` | `0x9290` | 135 | UnwindData |  |
| 57 | `WTSSetSessionInformationA` | `0x9320` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `WTSSetSessionInformationW` | `0x9320` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `WTSTerminateProcess` | `0x94A0` | 25 | UnwindData |  |
| 71 | `WTSVirtualChannelPurgeInput` | `0x9590` | 20 | UnwindData |  |
| 72 | `WTSVirtualChannelPurgeOutput` | `0x95B0` | 20 | UnwindData |  |
| 74 | `WTSVirtualChannelRead` | `0x95D0` | 271 | UnwindData |  |
| 75 | `WTSVirtualChannelWrite` | `0x96F0` | 172 | UnwindData |  |
| 47 | `WTSQueryUserConfigA` | `0x9E30` | 530 | UnwindData |  |
| 59 | `WTSSetUserConfigA` | `0xA050` | 476 | UnwindData |  |
| 15 | `WTSCreateListenerA` | `0xA580` | 276 | UnwindData |  |
| 16 | `WTSCreateListenerW` | `0xA6A0` | 2,007 | UnwindData |  |
| 19 | `WTSEnumerateListenersA` | `0xAE80` | 305 | UnwindData |  |
| 20 | `WTSEnumerateListenersW` | `0xAFC0` | 404 | UnwindData |  |
| 35 | `WTSGetListenerSecurityA` | `0xB160` | 227 | UnwindData |  |
| 36 | `WTSGetListenerSecurityW` | `0xB250` | 602 | UnwindData |  |
| 43 | `WTSQueryListenerConfigA` | `0xB4B0` | 307 | UnwindData |  |
| 54 | `WTSSetListenerSecurityA` | `0xB5F0` | 200 | UnwindData |  |
| 55 | `WTSSetListenerSecurityW` | `0xB6C0` | 435 | UnwindData |  |
| 7 | `WTSCloudAuthClose` | `0x14040` | 49 | UnwindData |  |
| 8 | `WTSCloudAuthConvertAssertionToSerializedUserCredential` | `0x14080` | 151 | UnwindData |  |
| 9 | `WTSCloudAuthDuplicateSerializedUserCredential` | `0x14120` | 119 | UnwindData |  |
| 10 | `WTSCloudAuthGetServerNonce` | `0x141A0` | 119 | UnwindData |  |
| 11 | `WTSCloudAuthNetworkLogonWithSerializedCredential` | `0x14220` | 134 | UnwindData |  |
| 12 | `WTSCloudAuthOpen` | `0x142B0` | 100 | UnwindData |  |
