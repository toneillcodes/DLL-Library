# Binary Specification: efscore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\efscore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a2a387de52d09463890c6f6fe21795d2982870bc0089f9544d6e855f13c5fca2`
* **Total Exported Functions:** 73

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EfsDllDplAppKeyCachingFeatureEnabled` | `0xE210` | 4,656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `EdpDllCredSvcControl` | `0xF440` | 323 | UnwindData |  |
| 4 | `EdpDllCredentialCreate` | `0xF590` | 238 | UnwindData |  |
| 5 | `EdpDllCredentialDelete` | `0xF690` | 247 | UnwindData |  |
| 6 | `EdpDllCredentialExists` | `0xF790` | 244 | UnwindData |  |
| 7 | `EdpDllCredentialQuery` | `0xF890` | 235 | UnwindData |  |
| 8 | `EdpDllDplUpgradePinInfo` | `0xF990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `EdpDllDplUpgradeVerifyUser` | `0xF990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `EdpDllDplUserCredentialsSet` | `0xF9A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `EdpDllDplUserUnlockComplete` | `0xF9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `EdpDllDplUserUnlockStart` | `0xF9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `EdpDllGetCredServiceState` | `0xF9D0` | 106 | UnwindData |  |
| 14 | `EdpDllGetLockSessionUnwrappedKey` | `0xFA40` | 595 | UnwindData |  |
| 15 | `EdpDllGetLockSessionWrappedKey` | `0xFCA0` | 93 | UnwindData |  |
| 18 | `EdpDllQueryDplEnforcedPolicyOwnerIds` | `0xFD10` | 213 | UnwindData |  |
| 19 | `EdpDllQueryRevokedPolicyOwnerIds` | `0xFDF0` | 226 | UnwindData |  |
| 21 | `EdpDllRmsClearKeys` | `0xFEE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `EdpDllRmsContainerizeFile` | `0xFF00` | 488 | UnwindData |  |
| 23 | `EdpDllRmsDecontainerizeFile` | `0x100F0` | 330 | UnwindData |  |
| 24 | `EdpDllRmsGetContainerIdentity` | `0x10240` | 815 | UnwindData |  |
| 28 | `EfsDllAddUsersToFileSrv` | `0x105C0` | 96 | UnwindData |  |
| 29 | `EfsDllAllocateHeap` | `0x10630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `EfsDllCheckFileAccess` | `0x10640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `EfsDllCloseFileRaw` | `0x10650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `EfsDllConstructEFS` | `0x10660` | 719 | UnwindData |  |
| 33 | `EfsDllDecryptFek` | `0x10940` | 65 | UnwindData |  |
| 34 | `EfsDllDecryptFileSrv` | `0x10990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `EfsDllDisabled` | `0x109A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `EfsDllDuplicateEncryptionInfoFileSrv` | `0x109B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `EfsDllEncryptFileSrv` | `0x109C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `EfsDllErrorToNtStatus` | `0x109D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `EfsDllFileKeyInfoSrv` | `0x109E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `EfsDllFreeHeap` | `0x109F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `EfsDllFreeUserInfo` | `0x10A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `EfsDllGetLocalFileName` | `0x10A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `EfsDllGetLogFile` | `0x10A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `EfsDllGetUserInfo` | `0x10A30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `EfsDllGetVolumeRoot` | `0x10A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `EfsDllIsConsumerProtectionEnforced` | `0x10A50` | 213 | UnwindData |  |
| 47 | `EfsDllIsNonEfsSKU` | `0x10B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `EfsDllLoadUserProfile` | `0x10B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `EfsDllMarkFileForDelete` | `0x10B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `EfsDllOefsAcquireExclusiveOperation` | `0x10B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `EfsDllOefsReleaseExclusiveOperation` | `0x10B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `EfsDllOnSessionChange` | `0x10B80` | 40 | UnwindData |  |
| 54 | `EfsDllOnSessionUserChange` | `0x10BB0` | 40 | UnwindData |  |
| 55 | `EfsDllOpenFileRaw` | `0x10BE0` | 25 | UnwindData |  |
| 56 | `EfsDllQueryProtectorsSrv` | `0x10C00` | 189 | UnwindData |  |
| 57 | `EfsDllQueryRecoveryAgentsSrv` | `0x10CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `EfsDllQueryUsersOnFileSrv` | `0x10CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `EfsDllReadFileRaw` | `0x10CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `EfsDllRemoveUsersFromFileSrv` | `0x10D00` | 80 | UnwindData |  |
| 62 | `EfsDllSetFileEncryptionKeySrv` | `0x10D60` | 80 | UnwindData |  |
| 63 | `EfsDllShareDecline` | `0x10DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `EfsDllSsoFlushUserCache` | `0x10DD0` | 33 | UnwindData |  |
| 65 | `EfsDllUnloadUserProfile` | `0x10E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `EfsDllUsePinForEncryptedFilesSrv` | `0x10E10` | 64 | UnwindData |  |
| 67 | `EfsDllValidateEfsStream` | `0x10E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `EfsDllWriteEncryptedFileWithHeader` | `0x10E70` | 159 | UnwindData |  |
| 69 | `EfsDllWriteFileRaw` | `0x10F20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `EfsInitialize` | `0x10F70` | 173 | UnwindData |  |
| 72 | `EfsUnInitialize` | `0x11030` | 47 | UnwindData |  |
| 61 | `EfsDllReprotectFile` | `0x15A20` | 1,239 | UnwindData |  |
| 71 | `EfsProcessRecoveryPolicy` | `0x20A90` | 614 | UnwindData |  |
| 73 | `EfsValidateEfsStream` | `0x27A60` | 211 | UnwindData |  |
| 20 | `EdpDllQueueFileForEncryption` | `0x45340` | 362 | UnwindData |  |
| 25 | `EdpDllServiceFileEncryptionQueue` | `0x454B0` | 168 | UnwindData |  |
| 2 | `EdpDllAllowFileAccessForProcess` | `0x4B860` | 434 | UnwindData |  |
| 16 | `EdpDllGetTfaCache` | `0x4BA20` | 552 | UnwindData |  |
| 17 | `EdpDllPurgeAppLearningEvents` | `0x4BE70` | 17 | UnwindData |  |
| 26 | `EdpWriteAppLearningLog` | `0x4BE90` | 434 | UnwindData |  |
| 27 | `EdpWriteSiteLearningLog` | `0x4C050` | 416 | UnwindData |  |
| 51 | `EfsDllOefsCheckSupportByFilePath` | `0x54B20` | 524 | UnwindData |  |
