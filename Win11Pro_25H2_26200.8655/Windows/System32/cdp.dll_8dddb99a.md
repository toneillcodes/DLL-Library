# Binary Specification: cdp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cdp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8dddb99a04499ed394363091b0e3d1075af6fd72971a96ec7bf0cd4b23216eaf`
* **Total Exported Functions:** 135

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 119 | `CDPRegisterActivityConflictResolverInternal` | `0xD040` | 247 | UnwindData |  |
| 12 | `CDPCreateActivityAsset` | `0xDF50` | 359 | UnwindData |  |
| 92 | `CDPGetActivityStoreForUser` | `0xEB40` | 241 | UnwindData |  |
| 23 | `CDPCreateAnonymousAccount` | `0x1AD30` | 289 | UnwindData |  |
| 8 | `CDPCreateAccountInternalForUser` | `0x28820` | 254 | UnwindData |  |
| 14 | `CDPCreateActivityStoreInfoInternal` | `0x44490` | 214 | UnwindData |  |
| 80 | `CDPCreateUuid` | `0x74180` | 1,128 | UnwindData |  |
| 121 | `CDPResume` | `0x7D250` | 350 | UnwindData |  |
| 131 | `CDPSuspend` | `0x7DD50` | 350 | UnwindData |  |
| 77 | `CDPCreateUserNotificationClientInternal` | `0x7E850` | 196 | UnwindData |  |
| 128 | `CDPShutdownBluetooth` | `0x7F720` | 98 | UnwindData |  |
| 83 | `CDPGetAccountProviderInternal` | `0xB4D50` | 254 | UnwindData |  |
| 39 | `CDPCreateCallbackNotifierInternal` | `0xD5C70` | 793 | UnwindData |  |
| 42 | `CDPCreateCrossPlatformAppId` | `0xD7BA0` | 160 | UnwindData |  |
| 13 | `CDPCreateActivityInternal` | `0xDDD40` | 390 | UnwindData |  |
| 4 | `CDPAccountFromWebAccount` | `0xE5150` | 2,019 | UnwindData |  |
| 70 | `CDPCreateSettingsInteropInternal` | `0xE5940` | 384 | UnwindData |  |
| 104 | `CDPGetResourceManager` | `0xE7330` | 155 | UnwindData |  |
| 113 | `CDPInitializeForService` | `0xEDA20` | 289 | UnwindData |  |
| 60 | `CDPCreateLoggedOnUserChangedNotifier` | `0xF31F0` | 276 | UnwindData |  |
| 7 | `CDPCreateAFSUserSettingsInternal` | `0xF42C0` | 180 | UnwindData |  |
| 93 | `CDPGetActivityStoreInternal` | `0xF8080` | 229 | UnwindData |  |
| 135 | `DllGetClassObject` | `0xFA3B0` | 53 | UnwindData |  |
| 19 | `CDPCreateActivityStoreReaderForUser` | `0xFB3C0` | 230 | UnwindData |  |
| 109 | `CDPGetUserActivitySettingsForUser` | `0xFBAD0` | 194 | UnwindData |  |
| 110 | `CDPGetUserActivitySettingsInternal` | `0xFD940` | 196 | UnwindData |  |
| 134 | `DllCanUnloadNow` | `0xFDE00` | 94,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `CDPInitialize` | `0x114FD0` | 207 | UnwindData |  |
| 79 | `CDPCreateUserServiceNotificationClientForUser` | `0x1186E0` | 95 | UnwindData |  |
| 117 | `CDPIsEnabled` | `0x12B150` | 92 | UnwindData |  |
| 136 | `DllRegisterServer` | `0x1417E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `DllUnregisterServer` | `0x141810` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetProxyDllInfo` | `0x141840` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CDPAcquireNetworkingInternal` | `0x142440` | 280 | UnwindData |  |
| 120 | `CDPReleaseNetworkingInternal` | `0x142560` | 130 | UnwindData |  |
| 9 | `CDPCreateAccountInternalWithStableUserId` | `0x142960` | 274 | UnwindData |  |
| 24 | `CDPCreateAnonymousAccountInternal` | `0x142A80` | 168 | UnwindData |  |
| 31 | `CDPCreateAzureActiveDirectoryAccount` | `0x142B30` | 136 | UnwindData |  |
| 64 | `CDPCreateMicrosoftAccount` | `0x142BC0` | 136 | UnwindData |  |
| 10 | `CDPCreateAccountProviderInternal` | `0x14B470` | 345 | UnwindData |  |
| 27 | `CDPCreateAppId` | `0x14BB00` | 236 | UnwindData |  |
| 107 | `CDPGetSystemAppId` | `0x14BC00` | 75 | UnwindData |  |
| 40 | `CDPCreateCloudNotification` | `0x14C6A0` | 229 | UnwindData |  |
| 41 | `CDPCreateComObjectInternal` | `0x14D0D0` | 318 | UnwindData |  |
| 43 | `CDPCreateCrossPlatformAppIdFromAppId` | `0x14DCE0` | 181 | UnwindData |  |
| 44 | `CDPCreateCurrentCrossPlatformAppId` | `0x14DDA0` | 231 | UnwindData |  |
| 57 | `CDPCreateEmptyAccountSettings` | `0x14EF00` | 181 | UnwindData |  |
| 85 | `CDPGetAccountsSettings` | `0x14EFC0` | 836 | UnwindData |  |
| 133 | `CDPWriteAccountSettings` | `0x14F310` | 734 | UnwindData |  |
| 58 | `CDPCreateEnvironmentManagerInternal` | `0x1504C0` | 192 | UnwindData |  |
| 59 | `CDPCreateHttpRequestInternal` | `0x151450` | 190 | UnwindData |  |
| 66 | `CDPCreatePlatformSettingsInternal` | `0x151900` | 208 | UnwindData |  |
| 68 | `CDPCreateResource` | `0x155480` | 760 | UnwindData |  |
| 69 | `CDPCreateResourceCollection` | `0x155780` | 1,025 | UnwindData |  |
| 103 | `CDPGetResourceHandler` | `0x155B90` | 233 | UnwindData |  |
| 73 | `CDPCreateTelemetryTask` | `0x1563F0` | 241 | UnwindData |  |
| 74 | `CDPCreateTelemetryTaskInternal` | `0x1564F0` | 241 | UnwindData |  |
| 76 | `CDPCreateUserInternal` | `0x157AC0` | 240 | UnwindData |  |
| 122 | `CDPSetAccountProviderInternal` | `0x158030` | 98 | UnwindData |  |
| 94 | `CDPGetCloudNotificationProviderInternal` | `0x159280` | 696 | UnwindData |  |
| 95 | `CDPGetCoreInitializer` | `0x159C30` | 156 | UnwindData |  |
| 100 | `CDPGetLogger` | `0x15ACC0` | 115 | UnwindData |  |
| 101 | `CDPGetNearShareAuthorizationPolicyOfInteractiveUser` | `0x15D260` | 225 | UnwindData |  |
| 105 | `CDPGetSDKAuthorizationPolicyOfInteractiveUser` | `0x15D350` | 225 | UnwindData |  |
| 111 | `CDPGetUserCollectionInternal` | `0x15DE10` | 144 | UnwindData |  |
| 118 | `CDPPreShutdown` | `0x15E410` | 286 | UnwindData |  |
| 125 | `CDPSetResourceConfigProvider` | `0x15E7C0` | 131 | UnwindData |  |
| 21 | `CDPCreateAllDevicesQuery` | `0x193CC0` | 193 | UnwindData |  |
| 22 | `CDPCreateAllDevicesQueryForUser` | `0x193D90` | 197 | UnwindData |  |
| 51 | `CDPCreateDeviceQuery` | `0x193E60` | 193 | UnwindData |  |
| 52 | `CDPCreateDeviceQueryForSessionInternal` | `0x193F30` | 359 | UnwindData |  |
| 53 | `CDPCreateDeviceQueryForUser` | `0x1940A0` | 197 | UnwindData |  |
| 54 | `CDPCreateDeviceQueryInternal` | `0x194170` | 252 | UnwindData |  |
| 55 | `CDPCreateDeviceQueryWithIdentity` | `0x194280` | 227 | UnwindData |  |
| 25 | `CDPCreateAppControlClient` | `0x19AD80` | 190 | UnwindData |  |
| 26 | `CDPCreateAppControlClientInternal` | `0x19AE50` | 190 | UnwindData |  |
| 28 | `CDPCreateAppRegistrationManager` | `0x19DCC0` | 193 | UnwindData |  |
| 29 | `CDPCreateAppRegistrationManagerForUser` | `0x19DD90` | 194 | UnwindData |  |
| 30 | `CDPCreateAppRegistrationManagerInternal` | `0x19DE60` | 154 | UnwindData |  |
| 34 | `CDPCreateBinaryClient` | `0x1A1190` | 145 | UnwindData |  |
| 35 | `CDPCreateBinaryClientInternal` | `0x1A1230` | 142 | UnwindData |  |
| 36 | `CDPCreateBinaryHost` | `0x1A3B70` | 26 | UnwindData |  |
| 37 | `CDPCreateBinaryHostInternal` | `0x1A3B90` | 214 | UnwindData |  |
| 38 | `CDPCreateBinaryHostWithSettings` | `0x1A3C70` | 285 | UnwindData |  |
| 45 | `CDPCreateDedupedDevice` | `0x1A4FC0` | 211 | UnwindData |  |
| 46 | `CDPCreateDedupedDeviceQuery` | `0x1A8610` | 193 | UnwindData |  |
| 47 | `CDPCreateDedupedDeviceQueryForUser` | `0x1A86E0` | 194 | UnwindData |  |
| 48 | `CDPCreateDedupedDeviceQueryInternal` | `0x1A87B0` | 196 | UnwindData |  |
| 49 | `CDPCreateDedupedDeviceQueryParameters` | `0x1A9E30` | 208 | UnwindData |  |
| 50 | `CDPCreateDeviceInternal` | `0x1AE8E0` | 372 | UnwindData |  |
| 124 | `CDPSetExtendedLocalDeviceStatus` | `0x1AEA60` | 4,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `CDPCreateDirectNotificationHost` | `0x1AFDE0` | 242 | UnwindData |  |
| 61 | `CDPCreateLoggedOnUserFamilyChangedNotifier` | `0x1B1790` | 274 | UnwindData |  |
| 62 | `CDPCreateMessagingHost` | `0x1B2730` | 203 | UnwindData |  |
| 63 | `CDPCreateMessagingHostInternal` | `0x1B2810` | 191 | UnwindData |  |
| 65 | `CDPCreateOrGetDdsRegistrationUserObjectInternal` | `0x1B3940` | 457 | UnwindData |  |
| 96 | `CDPGetDeviceCache` | `0x1B4510` | 193 | UnwindData |  |
| 97 | `CDPGetDeviceCacheInternal` | `0x1B45E0` | 196 | UnwindData |  |
| 98 | `CDPGetHost` | `0x1B51D0` | 103 | UnwindData |  |
| 102 | `CDPGetRelayInitializer` | `0x1B56D0` | 154 | UnwindData |  |
| 127 | `CDPShutdown` | `0x1B57E0` | 217 | UnwindData |  |
| 129 | `CDPStartCCSPolling` | `0x1B58C0` | 32 | UnwindData |  |
| 130 | `CDPStopCCSPolling` | `0x1B58F0` | 32 | UnwindData |  |
| 123 | `CDPSetAppControlHostCallback` | `0x1B9230` | 239 | UnwindData |  |
| 32 | `CDPCreateBeaconControl` | `0x279CC0` | 193 | UnwindData |  |
| 33 | `CDPCreateBeaconControlInternal` | `0x279D90` | 193 | UnwindData |  |
| 67 | `CDPCreateRemoteUserInternal` | `0x27A230` | 379 | UnwindData |  |
| 78 | `CDPCreateUserServiceNotificationClient` | `0x27ABF0` | 107 | UnwindData |  |
| 81 | `CDPFixAccounts` | `0x27DC10` | 414 | UnwindData |  |
| 84 | `CDPGetAccountsNeedAttention` | `0x27DDC0` | 313 | UnwindData |  |
| 106 | `CDPGetSGSocket` | `0x27E080` | 474 | UnwindData |  |
| 114 | `CDPInitializeSGPowerOnPacket` | `0x27E4E0` | 207 | UnwindData |  |
| 115 | `CDPInitializeUserService` | `0x281260` | 87 | UnwindData |  |
| 116 | `CDPInitializeUserServicePhase2` | `0x2812C0` | 72 | UnwindData |  |
| 132 | `CDPUninitializeUserService` | `0x281310` | 111 | UnwindData |  |
| 126 | `CDPSetServicePid` | `0x281430` | 24 | UnwindData |  |
| 6 | `CDPCreateAFSRegistrationClientInternal` | `0x2BB6C0` | 294 | UnwindData |  |
| 11 | `CDPCreateActivity` | `0x2BBBB0` | 387 | UnwindData |  |
| 75 | `CDPCreateTestActivityAsset` | `0x2BC740` | 221 | UnwindData |  |
| 15 | `CDPCreateActivityStoreInfoWatcher` | `0x2BE0C0` | 186 | UnwindData |  |
| 16 | `CDPCreateActivityStoreInfoWatcherForUser` | `0x2BE180` | 187 | UnwindData |  |
| 17 | `CDPCreateActivityStoreInfoWatcherInternal` | `0x2BE250` | 189 | UnwindData |  |
| 18 | `CDPCreateActivityStoreReader` | `0x2BF740` | 213 | UnwindData |  |
| 20 | `CDPCreateActivityStoreReaderInternal` | `0x2BF820` | 210 | UnwindData |  |
| 71 | `CDPCreateTask` | `0x2C1250` | 402 | UnwindData |  |
| 72 | `CDPCreateTaskInternal` | `0x2C13F0` | 408 | UnwindData |  |
| 82 | `CDPGetAFCInitializer` | `0x2C1A20` | 154 | UnwindData |  |
| 86 | `CDPGetActivityStore` | `0x2C7EF0` | 147 | UnwindData |  |
| 87 | `CDPGetActivityStoreForAccount` | `0x2C7F90` | 310 | UnwindData |  |
| 88 | `CDPGetActivityStoreForAccountInternal` | `0x2C80D0` | 239 | UnwindData |  |
| 89 | `CDPGetActivityStoreForStoreInfo` | `0x2C81D0` | 194 | UnwindData |  |
| 90 | `CDPGetActivityStoreForStoreInfoAndUser` | `0x2C82A0` | 336 | UnwindData |  |
| 91 | `CDPGetActivityStoreForStoreInfoInternal` | `0x2C8400` | 310 | UnwindData |  |
| 99 | `CDPGetInProcActivityStoreForUserToken` | `0x2C8540` | 310 | UnwindData |  |
| 108 | `CDPGetUserActivitySettings` | `0x2C93B0` | 193 | UnwindData |  |
