# Binary Specification: sppc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sppc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `139fdc103093b39779b802d439cbec7d4198b9095fefe2cdbf53b4228284894c`
* **Total Exported Functions:** 67

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `SLpAuthenticateGenuineTicketResponse` | `0xDB30` | 461 | UnwindData |  |
| 3 | `SLpBeginGenuineTicketTransaction` | `0xDD10` | 336 | UnwindData |  |
| 4 | `SLpClearActivationInProgress` | `0xDE70` | 236 | UnwindData |  |
| 5 | `SLpDepositDownlevelGenuineTicket` | `0xDF70` | 302 | UnwindData |  |
| 6 | `SLpDepositTokenActivationResponse` | `0xE0B0` | 389 | UnwindData |  |
| 7 | `SLpGenerateTokenActivationChallenge` | `0xE240` | 375 | UnwindData |  |
| 8 | `SLpGetGenuineBlob` | `0xE3C0` | 345 | UnwindData |  |
| 9 | `SLpGetGenuineLocal` | `0xE520` | 47 | UnwindData |  |
| 10 | `SLpGetLicenseAcquisitionInfo` | `0xE560` | 470 | UnwindData |  |
| 11 | `SLpGetMSPidInformation` | `0xE740` | 676 | UnwindData |  |
| 12 | `SLpGetMachineUGUID` | `0xE9F0` | 216 | UnwindData |  |
| 13 | `SLpGetTokenActivationGrantInfo` | `0xEAD0` | 490 | UnwindData |  |
| 14 | `SLpIAActivateProduct` | `0xECC0` | 237 | UnwindData |  |
| 15 | `SLpIsCurrentInstalledProductKeyDefaultKey` | `0xEDC0` | 244 | UnwindData |  |
| 16 | `SLpProcessVMPipeMessage` | `0xEEC0` | 396 | UnwindData |  |
| 17 | `SLpSetActivationInProgress` | `0xF060` | 233 | UnwindData |  |
| 18 | `SLpTriggerServiceWorker` | `0xF150` | 415 | UnwindData |  |
| 19 | `SLpVLActivateProduct` | `0xF300` | 215 | UnwindData |  |
| 20 | `SLClose` | `0x10FB0` | 41 | UnwindData |  |
| 21 | `SLConsumeRight` | `0x10FE0` | 277 | UnwindData |  |
| 22 | `SLDepositMigrationBlob` | `0x11100` | 260 | UnwindData |  |
| 23 | `SLDepositOfflineConfirmationId` | `0x11210` | 52 | UnwindData |  |
| 24 | `SLDepositOfflineConfirmationIdEx` | `0x11250` | 1,018 | UnwindData |  |
| 25 | `SLDepositStoreToken` | `0x11650` | 272 | UnwindData |  |
| 26 | `SLFireEvent` | `0x11770` | 284 | UnwindData |  |
| 27 | `SLGatherMigrationBlob` | `0x118A0` | 163 | UnwindData |  |
| 28 | `SLGatherMigrationBlobEx` | `0x11950` | 317 | UnwindData |  |
| 29 | `SLGenerateOfflineInstallationId` | `0x11AA0` | 47 | UnwindData |  |
| 30 | `SLGenerateOfflineInstallationIdEx` | `0x11AE0` | 404 | UnwindData |  |
| 31 | `SLGetActiveLicenseInfo` | `0x11C80` | 341 | UnwindData |  |
| 32 | `SLGetApplicationInformation` | `0x11DE0` | 140 | UnwindData |  |
| 33 | `SLGetApplicationPolicy` | `0x11E80` | 136 | UnwindData |  |
| 34 | `SLGetAuthenticationResult` | `0x11F10` | 334 | UnwindData |  |
| 35 | `SLGetEncryptedPIDEx` | `0x12070` | 353 | UnwindData |  |
| 36 | `SLGetGenuineInformation` | `0x121E0` | 481 | UnwindData |  |
| 37 | `SLGetInstalledProductKeyIds` | `0x123D0` | 414 | UnwindData |  |
| 38 | `SLGetLicense` | `0x12580` | 371 | UnwindData |  |
| 39 | `SLGetLicenseFileId` | `0x12700` | 320 | UnwindData |  |
| 40 | `SLGetLicenseInformation` | `0x12850` | 140 | UnwindData |  |
| 41 | `SLGetLicensingStatusInformation` | `0x128F0` | 399 | UnwindData |  |
| 42 | `SLGetPKeyId` | `0x12A90` | 424 | UnwindData |  |
| 43 | `SLGetPKeyInformation` | `0x12C40` | 140 | UnwindData |  |
| 44 | `SLGetPolicyInformation` | `0x12CE0` | 151 | UnwindData |  |
| 45 | `SLGetPolicyInformationDWORD` | `0x12D80` | 112 | UnwindData |  |
| 46 | `SLGetProductSkuInformation` | `0x12E00` | 137 | UnwindData |  |
| 47 | `SLGetSLIDList` | `0x12E90` | 458 | UnwindData |  |
| 48 | `SLGetServiceInformation` | `0x13060` | 74 | UnwindData |  |
| 49 | `SLInstallLicense` | `0x130B0` | 297 | UnwindData |  |
| 50 | `SLInstallProofOfPurchase` | `0x131E0` | 396 | UnwindData |  |
| 51 | `SLInstallProofOfPurchaseEx` | `0x13380` | 470 | UnwindData |  |
| 52 | `SLIsGenuineLocalEx` | `0x13560` | 222 | UnwindData |  |
| 53 | `SLLoadApplicationPolicies` | `0x13650` | 167 | UnwindData |  |
| 54 | `SLOpen` | `0x13700` | 241 | UnwindData |  |
| 55 | `SLPersistApplicationPolicies` | `0x13800` | 309 | UnwindData |  |
| 56 | `SLPersistRTSPayloadOverride` | `0x13940` | 348 | UnwindData |  |
| 57 | `SLReArm` | `0x13AB0` | 304 | UnwindData |  |
| 58 | `SLRegisterEvent` | `0x13BF0` | 133 | UnwindData |  |
| 59 | `SLRegisterPlugin` | `0x13C80` | 273 | UnwindData |  |
| 60 | `SLSetAuthenticationData` | `0x13DA0` | 308 | UnwindData |  |
| 61 | `SLSetCurrentProductKey` | `0x13EE0` | 277 | UnwindData |  |
| 62 | `SLSetGenuineInformation` | `0x14000` | 417 | UnwindData |  |
| 63 | `SLUninstallLicense` | `0x141B0` | 235 | UnwindData |  |
| 64 | `SLUninstallProofOfPurchase` | `0x142B0` | 224 | UnwindData |  |
| 65 | `SLUnloadApplicationPolicies` | `0x143A0` | 178 | UnwindData |  |
| 66 | `SLUnregisterEvent` | `0x14460` | 140 | UnwindData |  |
| 67 | `SLUnregisterPlugin` | `0x14500` | 219 | UnwindData |  |
| 1 | `SLCallServer` | `0x15670` | 526 | UnwindData |  |
