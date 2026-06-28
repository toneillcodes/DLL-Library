# Binary Specification: feclient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\feclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2a3ecfe73b3e570dcb927eee4eba6b61175113cbe2c0a6a0eec3b63eff6fdf41`
* **Total Exported Functions:** 60

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 52 | `EfsUtilGetCurrentKey` | `0x0` | - | Forwarded | Forwarded to: `efsutil._EfsUtilGetCurrentKey_Deprecated@16` |
| 1 | `DpQueryUserProtectorDescriptor` | `0x15730` | 370 | UnwindData |  |
| 2 | `DpQueryUserProtectorDescriptorInfo` | `0x158B0` | 373 | UnwindData |  |
| 3 | `EdpAllowFileAccessForProcess` | `0x15A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `EdpContainerizeFile` | `0x15A50` | 39 | UnwindData |  |
| 5 | `EdpCredentialCreate` | `0x15A80` | 338 | UnwindData |  |
| 6 | `EdpCredentialDelete` | `0x15BE0` | 38 | UnwindData |  |
| 7 | `EdpCredentialExists` | `0x15C10` | 286 | UnwindData |  |
| 8 | `EdpCredentialQuery` | `0x15D40` | 338 | UnwindData |  |
| 9 | `EdpDecontainerizeFile` | `0x15EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `EdpDplPolicyEnabledForUser` | `0x15EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `EdpDplStartCredServiceIfDplEnabledForUser` | `0x15ED0` | 115 | UnwindData |  |
| 12 | `EdpDplUpgradePinInfo` | `0x15F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `EdpDplUpgradeVerifyUser` | `0x15F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `EdpDplUserCredentialsSet` | `0x15F60` | 29 | UnwindData |  |
| 15 | `EdpDplUserUnlockComplete` | `0x15F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `EdpDplUserUnlockStart` | `0x15F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `EdpFree` | `0x15FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `EdpGetContainerIdentity` | `0x15FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `EdpGetCredServiceState` | `0x15FE0` | 91 | UnwindData |  |
| 20 | `EdpIsConsumerDataProtectionEnforced` | `0x16050` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `EdpIsConsumerDataProtectionSupported` | `0x16080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `EdpPurgeAppLearningEvents` | `0x16090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `EdpQueryCredServiceInfo` | `0x160A0` | 602 | UnwindData |  |
| 24 | `EdpQueryDplEnforcedPolicyOwnerIds` | `0x16300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `EdpQueryRevokedPolicyOwnerIds` | `0x16320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `EdpRmsClearKeys` | `0x16340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `EdpSetCredServiceInfo` | `0x16350` | 519 | UnwindData |  |
| 28 | `EdpUnprotectFile` | `0x16560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `EdpWriteLogSiteLearningEvents` | `0x16580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `EfsClientAddUsers` | `0x16590` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `EfsClientCloseFileRaw` | `0x168F0` | 140 | UnwindData |  |
| 32 | `EfsClientCopyFileRaw` | `0x16990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `EfsClientDecryptFile` | `0x169A0` | 208 | UnwindData |  |
| 34 | `EfsClientDuplicateEncryptionInfo` | `0x16A80` | 364 | UnwindData |  |
| 35 | `EfsClientEncryptFile` | `0x16C00` | 158 | UnwindData |  |
| 36 | `EfsClientEncryptFileEx` | `0x16CB0` | 122 | UnwindData |  |
| 37 | `EfsClientFileEncryptionStatus` | `0x16E70` | 134 | UnwindData |  |
| 38 | `EfsClientFreeHashList` | `0x16F70` | 214 | UnwindData |  |
| 39 | `EfsClientFreeKeyInfo` | `0x17050` | 75 | UnwindData |  |
| 40 | `EfsClientFreeProtectorList` | `0x170B0` | 229 | UnwindData |  |
| 41 | `EfsClientGetEncryptedFileVersion` | `0x171A0` | 131 | UnwindData |  |
| 42 | `EfsClientGetKeyInfo` | `0x17230` | 203 | UnwindData |  |
| 43 | `EfsClientOpenFileRaw` | `0x17310` | 303 | UnwindData |  |
| 44 | `EfsClientQueryProtectors` | `0x17450` | 123 | UnwindData |  |
| 45 | `EfsClientQueryRecoveryAgents` | `0x174E0` | 212 | UnwindData |  |
| 46 | `EfsClientQueryUsers` | `0x175C0` | 212 | UnwindData |  |
| 47 | `EfsClientReadFileRaw` | `0x176A0` | 70 | UnwindData |  |
| 48 | `EfsClientRemoveUsers` | `0x176F0` | 223 | UnwindData |  |
| 49 | `EfsClientWriteFileRaw` | `0x17900` | 53 | UnwindData |  |
| 50 | `EfsClientWriteFileWithHeaderRaw` | `0x17940` | 70 | UnwindData |  |
| 51 | `EfsReprotectFile` | `0x17990` | 116 | UnwindData |  |
| 53 | `EfsValidateTokenForConsumer` | `0x17A10` | 707 | UnwindData |  |
| 54 | `EfsValidateUserForConsumer` | `0x17CE0` | 418 | UnwindData |  |
| 55 | `FeClClearCaches` | `0x17E90` | 17 | UnwindData |  |
| 56 | `FeClQueryInfo` | `0x17EB0` | 153 | UnwindData |  |
| 57 | `FeClientInitialize` | `0x17F50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `GetLockSessionUnwrappedKey` | `0x17F70` | 355 | UnwindData |  |
| 59 | `GetLockSessionWrappedKey` | `0x180E0` | 370 | UnwindData |  |
| 60 | `OefsCheckSupport` | `0x18260` | 87,996 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
