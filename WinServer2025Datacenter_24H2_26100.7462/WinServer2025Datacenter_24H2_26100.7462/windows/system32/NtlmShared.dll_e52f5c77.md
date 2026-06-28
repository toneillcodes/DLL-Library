# Binary Specification: NtlmShared.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\NtlmShared.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e52f5c77ffdd33425e5dc6f49a28621cee091578290d47f6ec68d78461bce35b`
* **Total Exported Functions:** 43

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `MsvpCachePasswordsToCredential` | `0x8AB0` | 64 | UnwindData |  |
| 11 | `MsvpCalculateNtlm2Challenge` | `0x8B00` | 267 | UnwindData |  |
| 12 | `MsvpCalculateNtlm2ChallengeNew` | `0x8C20` | 425 | UnwindData |  |
| 13 | `MsvpCalculateNtlm2SessionKeys` | `0x8DD0` | 252 | UnwindData |  |
| 14 | `MsvpCalculateNtlm2SessionKeysNew` | `0x8EE0` | 413 | UnwindData |  |
| 15 | `MsvpCalculateNtlm3Owf` | `0x9090` | 318 | UnwindData |  |
| 16 | `MsvpCompareCredentials` | `0x93C0` | 209 | UnwindData |  |
| 17 | `MsvpComputeSaltedHashedPassword` | `0x94A0` | 403 | UnwindData |  |
| 18 | `MsvpCredentialToCachePasswords` | `0x9640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `MsvpDecryptDpapiMasterKey` | `0x9660` | 387 | UnwindData |  |
| 20 | `MsvpDeriveSecureCredKey` | `0x97F0` | 393 | UnwindData |  |
| 22 | `MsvpLm20GetNtlm3ChallengeResponse` | `0x9980` | 573 | UnwindData |  |
| 23 | `MsvpLm3Response` | `0x9BD0` | 546 | UnwindData |  |
| 24 | `MsvpLm3ResponseNew` | `0x9E00` | 890 | UnwindData |  |
| 27 | `MsvpMakeSecretPasswordNT5` | `0xA180` | 148 | UnwindData |  |
| 28 | `MsvpNtlm3Response` | `0xA220` | 546 | UnwindData |  |
| 29 | `MsvpNtlm3ResponseNew` | `0xA450` | 886 | UnwindData |  |
| 33 | `MsvpPutClearOwfsInPrimaryCredential` | `0xA7D0` | 292 | UnwindData |  |
| 1 | `MsvpAvlAdd` | `0xB1C0` | 191 | UnwindData |  |
| 2 | `MsvpAvlGet` | `0xB290` | 101 | UnwindData |  |
| 3 | `MsvpAvlGetFlags` | `0xB300` | 150 | UnwindData |  |
| 4 | `MsvpAvlGetTimestamp` | `0xB3A0` | 150 | UnwindData |  |
| 5 | `MsvpAvlInit` | `0xB440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MsvpAvlLen` | `0xB450` | 36 | UnwindData |  |
| 7 | `MsvpAvlSetFlags` | `0xB480` | 121 | UnwindData |  |
| 8 | `MsvpAvlSetTimestamp` | `0xB500` | 152 | UnwindData |  |
| 9 | `MsvpAvlToString` | `0xB5A0` | 155 | UnwindData |  |
| 21 | `MsvpGMSACred` | `0xB650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `NtlmSharedAllocate` | `0xB660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `NtlmSharedAllocatePrivateHeap` | `0xB680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `NtlmSharedCleanup` | `0xB6A0` | 116 | UnwindData |  |
| 41 | `NtlmSharedFree` | `0xB720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `NtlmSharedFreePrivateHeap` | `0xB740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `NtlmSharedInit` | `0xB760` | 707 | UnwindData |  |
| 34 | `MsvpUpdateSharedConfiguration` | `0xBAD0` | 106 | UnwindData |  |
| 37 | `NtLmAlterRtlEqualUnicodeString` | `0xBB40` | 94 | UnwindData |  |
| 25 | `MsvpLm3ValidateResponse` | `0xBBB0` | 210 | UnwindData |  |
| 26 | `MsvpLm3ValidateResponseNew` | `0xBC90` | 294 | UnwindData |  |
| 30 | `MsvpNtlm3ValidateResponse` | `0xBDC0` | 586 | UnwindData |  |
| 31 | `MsvpNtlm3ValidateResponseNew` | `0xC010` | 966 | UnwindData |  |
| 32 | `MsvpPasswordValidate` | `0xC3E0` | 2,260 | UnwindData |  |
| 35 | `MsvpValidateSupplementalCreds` | `0xCCC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `MsvpValidateSupplementalCredsBuffer` | `0xCCE0` | 183 | UnwindData |  |
