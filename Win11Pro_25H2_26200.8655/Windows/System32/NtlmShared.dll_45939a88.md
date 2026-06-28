# Binary Specification: NtlmShared.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\NtlmShared.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `45939a88868f7026eb0743be5621a668ba960c619ffb59c0b8018f50034db157`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `MsvpCachePasswordsToCredential` | `0x9CD0` | 64 | UnwindData |  |
| 11 | `MsvpCalculateNtlm2Challenge` | `0x9D20` | 425 | UnwindData |  |
| 12 | `MsvpCalculateNtlm2SessionKeys` | `0x9ED0` | 413 | UnwindData |  |
| 13 | `MsvpCalculateNtlm3Owf` | `0xA080` | 471 | UnwindData |  |
| 14 | `MsvpCompareCredentials` | `0xA260` | 209 | UnwindData |  |
| 15 | `MsvpComputeSaltedHashedPassword` | `0xA340` | 403 | UnwindData |  |
| 16 | `MsvpCredentialToCachePasswords` | `0xA4E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `MsvpDecryptDpapiMasterKey` | `0xA500` | 387 | UnwindData |  |
| 18 | `MsvpDeriveSecureCredKey` | `0xA690` | 393 | UnwindData |  |
| 20 | `MsvpLm20GetNtlm3ChallengeResponse` | `0xA820` | 529 | UnwindData |  |
| 21 | `MsvpLm3Response` | `0xAA40` | 890 | UnwindData |  |
| 23 | `MsvpMakeSecretPasswordNT5` | `0xADC0` | 148 | UnwindData |  |
| 24 | `MsvpNtlm3Response` | `0xAE60` | 886 | UnwindData |  |
| 27 | `MsvpPutClearOwfsInPrimaryCredential` | `0xB1E0` | 482 | UnwindData |  |
| 1 | `MsvpAvlAdd` | `0xBDC0` | 191 | UnwindData |  |
| 2 | `MsvpAvlGet` | `0xBE90` | 101 | UnwindData |  |
| 3 | `MsvpAvlGetFlags` | `0xBF00` | 150 | UnwindData |  |
| 4 | `MsvpAvlGetTimestamp` | `0xBFA0` | 150 | UnwindData |  |
| 5 | `MsvpAvlInit` | `0xC040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MsvpAvlLen` | `0xC050` | 36 | UnwindData |  |
| 7 | `MsvpAvlSetFlags` | `0xC080` | 121 | UnwindData |  |
| 8 | `MsvpAvlSetTimestamp` | `0xC100` | 152 | UnwindData |  |
| 9 | `MsvpAvlToString` | `0xC1A0` | 155 | UnwindData |  |
| 19 | `MsvpGMSACred` | `0xC250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `NtlmSharedAllocate` | `0xC260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `NtlmSharedAllocatePrivateHeap` | `0xC280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `NtlmSharedCleanup` | `0xC2A0` | 116 | UnwindData |  |
| 35 | `NtlmSharedFree` | `0xC320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `NtlmSharedFreePrivateHeap` | `0xC340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `NtlmSharedInit` | `0xC360` | 782 | UnwindData |  |
| 28 | `MsvpUpdateSharedConfiguration` | `0xC720` | 106 | UnwindData |  |
| 31 | `NtLmAlterRtlEqualUnicodeString` | `0xC790` | 94 | UnwindData |  |
| 22 | `MsvpLm3ValidateResponse` | `0xC800` | 294 | UnwindData |  |
| 25 | `MsvpNtlm3ValidateResponse` | `0xC930` | 968 | UnwindData |  |
| 26 | `MsvpPasswordValidate` | `0xCD00` | 2,106 | UnwindData |  |
| 29 | `MsvpValidateSupplementalCreds` | `0xD540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `MsvpValidateSupplementalCredsBuffer` | `0xD560` | 183 | UnwindData |  |
