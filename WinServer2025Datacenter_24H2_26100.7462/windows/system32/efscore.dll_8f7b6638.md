# Binary Specification: efscore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\efscore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8f7b66385aad29d6d31e55c24b6bd8e909847af6e8c4e324190831a15cc5b5e8`
* **Total Exported Functions:** 73

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EfsDllDplAppKeyCachingFeatureEnabled` | `0xE170` | 4,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `EdpDllCredSvcControl` | `0xF3A0` | 323 | UnwindData |  |
| 4 | `EdpDllCredentialCreate` | `0xF4F0` | 238 | UnwindData |  |
| 5 | `EdpDllCredentialDelete` | `0xF5F0` | 247 | UnwindData |  |
| 6 | `EdpDllCredentialExists` | `0xF6F0` | 244 | UnwindData |  |
| 7 | `EdpDllCredentialQuery` | `0xF7F0` | 235 | UnwindData |  |
| 8 | `EdpDllDplUpgradePinInfo` | `0xF8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `EdpDllDplUpgradeVerifyUser` | `0xF8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `EdpDllDplUserCredentialsSet` | `0xF900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `EdpDllDplUserUnlockComplete` | `0xF920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `EdpDllDplUserUnlockStart` | `0xF920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `EdpDllGetCredServiceState` | `0xF930` | 106 | UnwindData |  |
| 14 | `EdpDllGetLockSessionUnwrappedKey` | `0xF9A0` | 595 | UnwindData |  |
| 15 | `EdpDllGetLockSessionWrappedKey` | `0xFC00` | 93 | UnwindData |  |
| 18 | `EdpDllQueryDplEnforcedPolicyOwnerIds` | `0xFC70` | 213 | UnwindData |  |
| 19 | `EdpDllQueryRevokedPolicyOwnerIds` | `0xFD50` | 226 | UnwindData |  |
| 21 | `EdpDllRmsClearKeys` | `0xFE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `EdpDllRmsContainerizeFile` | `0xFE60` | 488 | UnwindData |  |
| 23 | `EdpDllRmsDecontainerizeFile` | `0x10050` | 330 | UnwindData |  |
| 24 | `EdpDllRmsGetContainerIdentity` | `0x101A0` | 815 | UnwindData |  |
| 28 | `EfsDllAddUsersToFileSrv` | `0x10520` | 96 | UnwindData |  |
| 29 | `EfsDllAllocateHeap` | `0x10590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `EfsDllCheckFileAccess` | `0x105A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `EfsDllCloseFileRaw` | `0x105B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `EfsDllConstructEFS` | `0x105C0` | 719 | UnwindData |  |
| 33 | `EfsDllDecryptFek` | `0x108A0` | 65 | UnwindData |  |
| 34 | `EfsDllDecryptFileSrv` | `0x108F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `EfsDllDisabled` | `0x10900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `EfsDllDuplicateEncryptionInfoFileSrv` | `0x10910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `EfsDllEncryptFileSrv` | `0x10920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `EfsDllErrorToNtStatus` | `0x10930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `EfsDllFileKeyInfoSrv` | `0x10940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `EfsDllFreeHeap` | `0x10950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `EfsDllFreeUserInfo` | `0x10960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `EfsDllGetLocalFileName` | `0x10970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `EfsDllGetLogFile` | `0x10980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `EfsDllGetUserInfo` | `0x10990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `EfsDllGetVolumeRoot` | `0x109A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `EfsDllIsConsumerProtectionEnforced` | `0x109B0` | 213 | UnwindData |  |
| 47 | `EfsDllIsNonEfsSKU` | `0x10A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `EfsDllLoadUserProfile` | `0x10AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `EfsDllMarkFileForDelete` | `0x10AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `EfsDllOefsAcquireExclusiveOperation` | `0x10AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `EfsDllOefsReleaseExclusiveOperation` | `0x10AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `EfsDllOnSessionChange` | `0x10AE0` | 40 | UnwindData |  |
| 54 | `EfsDllOnSessionUserChange` | `0x10B10` | 40 | UnwindData |  |
| 55 | `EfsDllOpenFileRaw` | `0x10B40` | 25 | UnwindData |  |
| 56 | `EfsDllQueryProtectorsSrv` | `0x10B60` | 189 | UnwindData |  |
| 57 | `EfsDllQueryRecoveryAgentsSrv` | `0x10C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `EfsDllQueryUsersOnFileSrv` | `0x10C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `EfsDllReadFileRaw` | `0x10C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `EfsDllRemoveUsersFromFileSrv` | `0x10C60` | 80 | UnwindData |  |
| 62 | `EfsDllSetFileEncryptionKeySrv` | `0x10CC0` | 80 | UnwindData |  |
| 63 | `EfsDllShareDecline` | `0x10D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `EfsDllSsoFlushUserCache` | `0x10D30` | 33 | UnwindData |  |
| 65 | `EfsDllUnloadUserProfile` | `0x10D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `EfsDllUsePinForEncryptedFilesSrv` | `0x10D70` | 64 | UnwindData |  |
| 67 | `EfsDllValidateEfsStream` | `0x10DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `EfsDllWriteEncryptedFileWithHeader` | `0x10DD0` | 159 | UnwindData |  |
| 69 | `EfsDllWriteFileRaw` | `0x10E80` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `EfsInitialize` | `0x10ED0` | 173 | UnwindData |  |
| 72 | `EfsUnInitialize` | `0x10F90` | 47 | UnwindData |  |
| 61 | `EfsDllReprotectFile` | `0x15980` | 1,239 | UnwindData |  |
| 71 | `EfsProcessRecoveryPolicy` | `0x209F0` | 614 | UnwindData |  |
| 73 | `EfsValidateEfsStream` | `0x279C0` | 211 | UnwindData |  |
| 20 | `EdpDllQueueFileForEncryption` | `0x450B0` | 362 | UnwindData |  |
| 25 | `EdpDllServiceFileEncryptionQueue` | `0x45220` | 168 | UnwindData |  |
| 2 | `EdpDllAllowFileAccessForProcess` | `0x4B5D0` | 434 | UnwindData |  |
| 16 | `EdpDllGetTfaCache` | `0x4B790` | 552 | UnwindData |  |
| 17 | `EdpDllPurgeAppLearningEvents` | `0x4BBE0` | 17 | UnwindData |  |
| 26 | `EdpWriteAppLearningLog` | `0x4BC00` | 434 | UnwindData |  |
| 27 | `EdpWriteSiteLearningLog` | `0x4BDC0` | 416 | UnwindData |  |
| 51 | `EfsDllOefsCheckSupportByFilePath` | `0x548C0` | 524 | UnwindData |  |
