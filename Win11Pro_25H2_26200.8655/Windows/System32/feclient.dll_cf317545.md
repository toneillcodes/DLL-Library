# Binary Specification: feclient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\feclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cf317545849c08bd72ecdd6578d904cd444fc9fe351feedbacfcc535aa8c4591`
* **Total Exported Functions:** 60

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 52 | `EfsUtilGetCurrentKey` | `0x0` | - | Forwarded | Forwarded to: `efsutil._EfsUtilGetCurrentKey_Deprecated@16` |
| 1 | `DpQueryUserProtectorDescriptor` | `0x15880` | 370 | UnwindData |  |
| 2 | `DpQueryUserProtectorDescriptorInfo` | `0x15A00` | 373 | UnwindData |  |
| 3 | `EdpAllowFileAccessForProcess` | `0x15B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `EdpContainerizeFile` | `0x15BA0` | 39 | UnwindData |  |
| 5 | `EdpCredentialCreate` | `0x15BD0` | 338 | UnwindData |  |
| 6 | `EdpCredentialDelete` | `0x15D30` | 38 | UnwindData |  |
| 7 | `EdpCredentialExists` | `0x15D60` | 286 | UnwindData |  |
| 8 | `EdpCredentialQuery` | `0x15E90` | 338 | UnwindData |  |
| 9 | `EdpDecontainerizeFile` | `0x15FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `EdpDplPolicyEnabledForUser` | `0x16010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `EdpDplStartCredServiceIfDplEnabledForUser` | `0x16020` | 115 | UnwindData |  |
| 12 | `EdpDplUpgradePinInfo` | `0x160A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `EdpDplUpgradeVerifyUser` | `0x160A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `EdpDplUserCredentialsSet` | `0x160B0` | 29 | UnwindData |  |
| 15 | `EdpDplUserUnlockComplete` | `0x160E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `EdpDplUserUnlockStart` | `0x160E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `EdpFree` | `0x160F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `EdpGetContainerIdentity` | `0x16110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `EdpGetCredServiceState` | `0x16130` | 91 | UnwindData |  |
| 20 | `EdpIsConsumerDataProtectionEnforced` | `0x161A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `EdpIsConsumerDataProtectionSupported` | `0x161D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `EdpPurgeAppLearningEvents` | `0x161E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `EdpQueryCredServiceInfo` | `0x161F0` | 602 | UnwindData |  |
| 24 | `EdpQueryDplEnforcedPolicyOwnerIds` | `0x16450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `EdpQueryRevokedPolicyOwnerIds` | `0x16470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `EdpRmsClearKeys` | `0x16490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `EdpSetCredServiceInfo` | `0x164A0` | 519 | UnwindData |  |
| 28 | `EdpUnprotectFile` | `0x166B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `EdpWriteLogSiteLearningEvents` | `0x166D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `EfsClientAddUsers` | `0x166E0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `EfsClientCloseFileRaw` | `0x16A40` | 140 | UnwindData |  |
| 32 | `EfsClientCopyFileRaw` | `0x16AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `EfsClientDecryptFile` | `0x16AF0` | 208 | UnwindData |  |
| 34 | `EfsClientDuplicateEncryptionInfo` | `0x16BD0` | 364 | UnwindData |  |
| 35 | `EfsClientEncryptFile` | `0x16D50` | 158 | UnwindData |  |
| 36 | `EfsClientEncryptFileEx` | `0x16E00` | 122 | UnwindData |  |
| 37 | `EfsClientFileEncryptionStatus` | `0x16FC0` | 134 | UnwindData |  |
| 38 | `EfsClientFreeHashList` | `0x170C0` | 214 | UnwindData |  |
| 39 | `EfsClientFreeKeyInfo` | `0x171A0` | 75 | UnwindData |  |
| 40 | `EfsClientFreeProtectorList` | `0x17200` | 229 | UnwindData |  |
| 41 | `EfsClientGetEncryptedFileVersion` | `0x172F0` | 131 | UnwindData |  |
| 42 | `EfsClientGetKeyInfo` | `0x17380` | 203 | UnwindData |  |
| 43 | `EfsClientOpenFileRaw` | `0x17460` | 303 | UnwindData |  |
| 44 | `EfsClientQueryProtectors` | `0x175A0` | 123 | UnwindData |  |
| 45 | `EfsClientQueryRecoveryAgents` | `0x17630` | 212 | UnwindData |  |
| 46 | `EfsClientQueryUsers` | `0x17710` | 212 | UnwindData |  |
| 47 | `EfsClientReadFileRaw` | `0x177F0` | 70 | UnwindData |  |
| 48 | `EfsClientRemoveUsers` | `0x17840` | 223 | UnwindData |  |
| 49 | `EfsClientWriteFileRaw` | `0x17A50` | 53 | UnwindData |  |
| 50 | `EfsClientWriteFileWithHeaderRaw` | `0x17A90` | 70 | UnwindData |  |
| 51 | `EfsReprotectFile` | `0x17AE0` | 116 | UnwindData |  |
| 53 | `EfsValidateTokenForConsumer` | `0x17B60` | 707 | UnwindData |  |
| 54 | `EfsValidateUserForConsumer` | `0x17E30` | 418 | UnwindData |  |
| 55 | `FeClClearCaches` | `0x17FE0` | 17 | UnwindData |  |
| 56 | `FeClQueryInfo` | `0x18000` | 153 | UnwindData |  |
| 57 | `FeClientInitialize` | `0x180A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `GetLockSessionUnwrappedKey` | `0x180C0` | 355 | UnwindData |  |
| 59 | `GetLockSessionWrappedKey` | `0x18230` | 370 | UnwindData |  |
| 60 | `OefsCheckSupport` | `0x183B0` | 90,524 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
