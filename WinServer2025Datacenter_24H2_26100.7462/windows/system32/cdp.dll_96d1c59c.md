# Binary Specification: cdp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cdp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `96d1c59c9dd13a95b040dfa4ad324787823953cc47b19d4151b9b0abc1c35927`
* **Total Exported Functions:** 135

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 119 | `CDPRegisterActivityConflictResolverInternal` | `0xD030` | 247 | UnwindData |  |
| 12 | `CDPCreateActivityAsset` | `0xDF40` | 359 | UnwindData |  |
| 92 | `CDPGetActivityStoreForUser` | `0xEB30` | 241 | UnwindData |  |
| 23 | `CDPCreateAnonymousAccount` | `0x1AD20` | 289 | UnwindData |  |
| 8 | `CDPCreateAccountInternalForUser` | `0x28820` | 254 | UnwindData |  |
| 80 | `CDPCreateUuid` | `0x4B9B0` | 1,128 | UnwindData |  |
| 14 | `CDPCreateActivityStoreInfoInternal` | `0x7C3A0` | 214 | UnwindData |  |
| 121 | `CDPResume` | `0x8C160` | 350 | UnwindData |  |
| 131 | `CDPSuspend` | `0x8CC60` | 350 | UnwindData |  |
| 77 | `CDPCreateUserNotificationClientInternal` | `0x8D760` | 196 | UnwindData |  |
| 128 | `CDPShutdownBluetooth` | `0x8E630` | 98 | UnwindData |  |
| 83 | `CDPGetAccountProviderInternal` | `0xB36E0` | 254 | UnwindData |  |
| 39 | `CDPCreateCallbackNotifierInternal` | `0xD48A0` | 793 | UnwindData |  |
| 42 | `CDPCreateCrossPlatformAppId` | `0xD68B0` | 160 | UnwindData |  |
| 13 | `CDPCreateActivityInternal` | `0xDCDF0` | 390 | UnwindData |  |
| 4 | `CDPAccountFromWebAccount` | `0xE4C40` | 2,019 | UnwindData |  |
| 70 | `CDPCreateSettingsInteropInternal` | `0xE5430` | 384 | UnwindData |  |
| 104 | `CDPGetResourceManager` | `0xE6E20` | 155 | UnwindData |  |
| 113 | `CDPInitializeForService` | `0xEDC20` | 289 | UnwindData |  |
| 60 | `CDPCreateLoggedOnUserChangedNotifier` | `0xF38D0` | 276 | UnwindData |  |
| 7 | `CDPCreateAFSUserSettingsInternal` | `0xF4970` | 180 | UnwindData |  |
| 93 | `CDPGetActivityStoreInternal` | `0xF8800` | 229 | UnwindData |  |
| 135 | `DllGetClassObject` | `0xFAB20` | 53 | UnwindData |  |
| 19 | `CDPCreateActivityStoreReaderForUser` | `0xFBB30` | 230 | UnwindData |  |
| 109 | `CDPGetUserActivitySettingsForUser` | `0xFC240` | 194 | UnwindData |  |
| 110 | `CDPGetUserActivitySettingsInternal` | `0xFE050` | 196 | UnwindData |  |
| 134 | `DllCanUnloadNow` | `0xFE510` | 93,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `CDPInitialize` | `0x1152E0` | 207 | UnwindData |  |
| 79 | `CDPCreateUserServiceNotificationClientForUser` | `0x118B80` | 95 | UnwindData |  |
| 117 | `CDPIsEnabled` | `0x12B500` | 92 | UnwindData |  |
| 136 | `DllRegisterServer` | `0x141B40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `DllUnregisterServer` | `0x141B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetProxyDllInfo` | `0x141BA0` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CDPAcquireNetworkingInternal` | `0x1427A0` | 280 | UnwindData |  |
| 120 | `CDPReleaseNetworkingInternal` | `0x1428C0` | 130 | UnwindData |  |
| 9 | `CDPCreateAccountInternalWithStableUserId` | `0x142CC0` | 274 | UnwindData |  |
| 24 | `CDPCreateAnonymousAccountInternal` | `0x142DE0` | 168 | UnwindData |  |
| 31 | `CDPCreateAzureActiveDirectoryAccount` | `0x142E90` | 136 | UnwindData |  |
| 64 | `CDPCreateMicrosoftAccount` | `0x142F20` | 136 | UnwindData |  |
| 10 | `CDPCreateAccountProviderInternal` | `0x14CC20` | 345 | UnwindData |  |
| 27 | `CDPCreateAppId` | `0x14D7E0` | 236 | UnwindData |  |
| 107 | `CDPGetSystemAppId` | `0x14D8E0` | 75 | UnwindData |  |
| 40 | `CDPCreateCloudNotification` | `0x14E380` | 229 | UnwindData |  |
| 41 | `CDPCreateComObjectInternal` | `0x14EDB0` | 318 | UnwindData |  |
| 43 | `CDPCreateCrossPlatformAppIdFromAppId` | `0x14F9C0` | 181 | UnwindData |  |
| 44 | `CDPCreateCurrentCrossPlatformAppId` | `0x14FA80` | 231 | UnwindData |  |
| 57 | `CDPCreateEmptyAccountSettings` | `0x150BE0` | 181 | UnwindData |  |
| 85 | `CDPGetAccountsSettings` | `0x150CA0` | 836 | UnwindData |  |
| 133 | `CDPWriteAccountSettings` | `0x150FF0` | 734 | UnwindData |  |
| 58 | `CDPCreateEnvironmentManagerInternal` | `0x1521A0` | 192 | UnwindData |  |
| 59 | `CDPCreateHttpRequestInternal` | `0x153130` | 190 | UnwindData |  |
| 66 | `CDPCreatePlatformSettingsInternal` | `0x1535E0` | 208 | UnwindData |  |
| 68 | `CDPCreateResource` | `0x157160` | 760 | UnwindData |  |
| 69 | `CDPCreateResourceCollection` | `0x157460` | 1,025 | UnwindData |  |
| 103 | `CDPGetResourceHandler` | `0x157870` | 233 | UnwindData |  |
| 73 | `CDPCreateTelemetryTask` | `0x1580D0` | 241 | UnwindData |  |
| 74 | `CDPCreateTelemetryTaskInternal` | `0x1581D0` | 241 | UnwindData |  |
| 76 | `CDPCreateUserInternal` | `0x1597A0` | 240 | UnwindData |  |
| 122 | `CDPSetAccountProviderInternal` | `0x159D10` | 98 | UnwindData |  |
| 94 | `CDPGetCloudNotificationProviderInternal` | `0x15AF60` | 696 | UnwindData |  |
| 95 | `CDPGetCoreInitializer` | `0x15B910` | 156 | UnwindData |  |
| 100 | `CDPGetLogger` | `0x15C9A0` | 115 | UnwindData |  |
| 101 | `CDPGetNearShareAuthorizationPolicyOfInteractiveUser` | `0x15EF40` | 225 | UnwindData |  |
| 105 | `CDPGetSDKAuthorizationPolicyOfInteractiveUser` | `0x15F030` | 225 | UnwindData |  |
| 111 | `CDPGetUserCollectionInternal` | `0x15FAF0` | 144 | UnwindData |  |
| 118 | `CDPPreShutdown` | `0x1600F0` | 286 | UnwindData |  |
| 125 | `CDPSetResourceConfigProvider` | `0x1604A0` | 131 | UnwindData |  |
| 21 | `CDPCreateAllDevicesQuery` | `0x196220` | 193 | UnwindData |  |
| 22 | `CDPCreateAllDevicesQueryForUser` | `0x1962F0` | 197 | UnwindData |  |
| 51 | `CDPCreateDeviceQuery` | `0x1963C0` | 193 | UnwindData |  |
| 52 | `CDPCreateDeviceQueryForSessionInternal` | `0x196490` | 359 | UnwindData |  |
| 53 | `CDPCreateDeviceQueryForUser` | `0x196600` | 197 | UnwindData |  |
| 54 | `CDPCreateDeviceQueryInternal` | `0x1966D0` | 252 | UnwindData |  |
| 55 | `CDPCreateDeviceQueryWithIdentity` | `0x1967E0` | 227 | UnwindData |  |
| 25 | `CDPCreateAppControlClient` | `0x19D2E0` | 190 | UnwindData |  |
| 26 | `CDPCreateAppControlClientInternal` | `0x19D3B0` | 190 | UnwindData |  |
| 28 | `CDPCreateAppRegistrationManager` | `0x1A0220` | 193 | UnwindData |  |
| 29 | `CDPCreateAppRegistrationManagerForUser` | `0x1A02F0` | 194 | UnwindData |  |
| 30 | `CDPCreateAppRegistrationManagerInternal` | `0x1A03C0` | 154 | UnwindData |  |
| 34 | `CDPCreateBinaryClient` | `0x1A36C0` | 145 | UnwindData |  |
| 35 | `CDPCreateBinaryClientInternal` | `0x1A3760` | 142 | UnwindData |  |
| 36 | `CDPCreateBinaryHost` | `0x1A6720` | 26 | UnwindData |  |
| 37 | `CDPCreateBinaryHostInternal` | `0x1A6740` | 214 | UnwindData |  |
| 38 | `CDPCreateBinaryHostWithSettings` | `0x1A6820` | 285 | UnwindData |  |
| 45 | `CDPCreateDedupedDevice` | `0x1A7A90` | 211 | UnwindData |  |
| 46 | `CDPCreateDedupedDeviceQuery` | `0x1AB0E0` | 193 | UnwindData |  |
| 47 | `CDPCreateDedupedDeviceQueryForUser` | `0x1AB1B0` | 194 | UnwindData |  |
| 48 | `CDPCreateDedupedDeviceQueryInternal` | `0x1AB280` | 196 | UnwindData |  |
| 49 | `CDPCreateDedupedDeviceQueryParameters` | `0x1AC900` | 208 | UnwindData |  |
| 50 | `CDPCreateDeviceInternal` | `0x1B13B0` | 372 | UnwindData |  |
| 124 | `CDPSetExtendedLocalDeviceStatus` | `0x1B1530` | 4,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `CDPCreateDirectNotificationHost` | `0x1B28B0` | 242 | UnwindData |  |
| 61 | `CDPCreateLoggedOnUserFamilyChangedNotifier` | `0x1B4260` | 274 | UnwindData |  |
| 62 | `CDPCreateMessagingHost` | `0x1B5270` | 203 | UnwindData |  |
| 63 | `CDPCreateMessagingHostInternal` | `0x1B5350` | 191 | UnwindData |  |
| 65 | `CDPCreateOrGetDdsRegistrationUserObjectInternal` | `0x1B6480` | 457 | UnwindData |  |
| 96 | `CDPGetDeviceCache` | `0x1B7050` | 193 | UnwindData |  |
| 97 | `CDPGetDeviceCacheInternal` | `0x1B7120` | 196 | UnwindData |  |
| 98 | `CDPGetHost` | `0x1B7D10` | 103 | UnwindData |  |
| 102 | `CDPGetRelayInitializer` | `0x1B8210` | 154 | UnwindData |  |
| 127 | `CDPShutdown` | `0x1B8320` | 217 | UnwindData |  |
| 129 | `CDPStartCCSPolling` | `0x1B8400` | 32 | UnwindData |  |
| 130 | `CDPStopCCSPolling` | `0x1B8430` | 32 | UnwindData |  |
| 123 | `CDPSetAppControlHostCallback` | `0x1BBD70` | 239 | UnwindData |  |
| 32 | `CDPCreateBeaconControl` | `0x27ABD0` | 193 | UnwindData |  |
| 33 | `CDPCreateBeaconControlInternal` | `0x27ACA0` | 193 | UnwindData |  |
| 67 | `CDPCreateRemoteUserInternal` | `0x27B140` | 379 | UnwindData |  |
| 78 | `CDPCreateUserServiceNotificationClient` | `0x27BB00` | 107 | UnwindData |  |
| 81 | `CDPFixAccounts` | `0x27EB20` | 414 | UnwindData |  |
| 84 | `CDPGetAccountsNeedAttention` | `0x27ECD0` | 313 | UnwindData |  |
| 106 | `CDPGetSGSocket` | `0x27EF90` | 474 | UnwindData |  |
| 114 | `CDPInitializeSGPowerOnPacket` | `0x27F3F0` | 207 | UnwindData |  |
| 115 | `CDPInitializeUserService` | `0x282170` | 87 | UnwindData |  |
| 116 | `CDPInitializeUserServicePhase2` | `0x2821D0` | 72 | UnwindData |  |
| 132 | `CDPUninitializeUserService` | `0x282220` | 111 | UnwindData |  |
| 126 | `CDPSetServicePid` | `0x282340` | 24 | UnwindData |  |
| 6 | `CDPCreateAFSRegistrationClientInternal` | `0x2BC8E0` | 294 | UnwindData |  |
| 11 | `CDPCreateActivity` | `0x2BCDD0` | 387 | UnwindData |  |
| 75 | `CDPCreateTestActivityAsset` | `0x2BD960` | 221 | UnwindData |  |
| 15 | `CDPCreateActivityStoreInfoWatcher` | `0x2BF2E0` | 186 | UnwindData |  |
| 16 | `CDPCreateActivityStoreInfoWatcherForUser` | `0x2BF3A0` | 187 | UnwindData |  |
| 17 | `CDPCreateActivityStoreInfoWatcherInternal` | `0x2BF470` | 189 | UnwindData |  |
| 18 | `CDPCreateActivityStoreReader` | `0x2C0960` | 213 | UnwindData |  |
| 20 | `CDPCreateActivityStoreReaderInternal` | `0x2C0A40` | 210 | UnwindData |  |
| 71 | `CDPCreateTask` | `0x2C2470` | 402 | UnwindData |  |
| 72 | `CDPCreateTaskInternal` | `0x2C2610` | 408 | UnwindData |  |
| 82 | `CDPGetAFCInitializer` | `0x2C2C40` | 154 | UnwindData |  |
| 86 | `CDPGetActivityStore` | `0x2C9110` | 147 | UnwindData |  |
| 87 | `CDPGetActivityStoreForAccount` | `0x2C91B0` | 310 | UnwindData |  |
| 88 | `CDPGetActivityStoreForAccountInternal` | `0x2C92F0` | 239 | UnwindData |  |
| 89 | `CDPGetActivityStoreForStoreInfo` | `0x2C93F0` | 194 | UnwindData |  |
| 90 | `CDPGetActivityStoreForStoreInfoAndUser` | `0x2C94C0` | 336 | UnwindData |  |
| 91 | `CDPGetActivityStoreForStoreInfoInternal` | `0x2C9620` | 310 | UnwindData |  |
| 99 | `CDPGetInProcActivityStoreForUserToken` | `0x2C9760` | 310 | UnwindData |  |
| 108 | `CDPGetUserActivitySettings` | `0x2CA5D0` | 193 | UnwindData |  |
