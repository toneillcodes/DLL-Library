# Binary Specification: KerbClientShared.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\KerbClientShared.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `74d45625c982daa2343bf70beeee3b973a064da651af4ec164b9281929ff734f`
* **Total Exported Functions:** 38

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `KerbClientPackAsn1Buffer` | `0x1300` | 1,093 | UnwindData |  |
| 27 | `KerbClientUnpackAsn1BufferVoid` | `0x1750` | 118 | UnwindData |  |
| 13 | `KerbClientComputeTgsChecksum` | `0x1C90` | 13 | UnwindData |  |
| 19 | `KerbClientFreeStoredCred` | `0x6580` | 62 | UnwindData |  |
| 17 | `KerbClientDuplicateStoredCred` | `0x9170` | 314 | UnwindData |  |
| 2 | `KerbClientAlloc` | `0x9F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `KerbClientFreeSupplementalCredentials` | `0x9F20` | 35 | UnwindData |  |
| 3 | `KerbClientAllocateStoredCred` | `0xA0C0` | 47 | UnwindData |  |
| 11 | `KerbClientBuildStrengthenedReplyKey` | `0xA3F0` | 438 | UnwindData |  |
| 18 | `KerbClientFree` | `0xAC40` | 2,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `KerbClientVerifyFastArmoredKdcReply` | `0xB7F0` | 3,011 | UnwindData |  |
| 5 | `KerbClientBuildEncryptedAuthData` | `0xC3C0` | 489 | UnwindData |  |
| 30 | `KerbClientVerifyChecksum` | `0xC5B0` | 1,176 | UnwindData |  |
| 14 | `KerbClientDecryptApReply` | `0xCA50` | 1,469 | UnwindData |  |
| 21 | `KerbClientPackApReply` | `0xD020` | 23 | UnwindData |  |
| 12 | `KerbClientBuildTicketArmorKey` | `0xD800` | 418 | UnwindData |  |
| 26 | `KerbClientTransformStoredCred` | `0xE040` | 328 | UnwindData |  |
| 9 | `KerbClientBuildKerbPriv` | `0x11F30` | 422 | UnwindData |  |
| 24 | `KerbClientSharedCleanup` | `0x120E0` | 116 | UnwindData |  |
| 25 | `KerbClientSharedInit` | `0x12160` | 160 | UnwindData |  |
| 35 | `KerbClientVerifyPrivMessage` | `0x12210` | 572 | UnwindData |  |
| 10 | `KerbClientBuildKeyList` | `0x160B0` | 2,844 | UnwindData |  |
| 6 | `KerbClientBuildExplicitArmorKey` | `0x174C0` | 309 | UnwindData |  |
| 7 | `KerbClientBuildFastArmoredKdcRequest` | `0x17600` | 1,402 | UnwindData |  |
| 8 | `KerbClientBuildFastChallenge` | `0x17B80` | 712 | UnwindData |  |
| 16 | `KerbClientDeriveFastChallengeKey` | `0x17E50` | 50 | UnwindData |  |
| 31 | `KerbClientVerifyEncryptedChallengePaData` | `0x17E90` | 529 | UnwindData |  |
| 33 | `KerbClientVerifyFastArmoredKerbError` | `0x180B0` | 1,337 | UnwindData |  |
| 34 | `KerbClientVerifyFastArmoredTgsReply` | `0x185F0` | 251 | UnwindData |  |
| 4 | `KerbClientBuildAsReqAuthenticator` | `0x189A0` | 621 | UnwindData |  |
| 15 | `KerbClientDecryptPacCredentials` | `0x18C20` | 369 | UnwindData |  |
| 23 | `KerbClientParseKeyListReplyPaData` | `0x190F0` | 487 | UnwindData |  |
| 28 | `KerbClientUnpackKdcReplyBody` | `0x192E0` | 1,147 | UnwindData |  |
| 1 | `KerbClient3961UpdateSharedConfiguration` | `0x19770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `KerbClientUpdateSharedConfiguration` | `0x19790` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `KerbGetFlagsForKdcReply` | `0x19940` | 393 | UnwindData |  |
| 37 | `KerbKdcReplyContainsTgt` | `0x19AD0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `KerbPackKdcReplyWithEncryptedSessionKey` | `0x19B10` | 387 | UnwindData |  |
