# Binary Specification: KerbClientShared.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\KerbClientShared.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `96d2e60ffabcfc42541b3472d4c5e14b6c96677d63c75029730edf185f4a2503`
* **Total Exported Functions:** 38

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `KerbClientPackAsn1Buffer` | `0x12A0` | 1,093 | UnwindData |  |
| 27 | `KerbClientUnpackAsn1BufferVoid` | `0x16F0` | 118 | UnwindData |  |
| 13 | `KerbClientComputeTgsChecksum` | `0x1C30` | 13 | UnwindData |  |
| 19 | `KerbClientFreeStoredCred` | `0x6520` | 62 | UnwindData |  |
| 17 | `KerbClientDuplicateStoredCred` | `0x9110` | 314 | UnwindData |  |
| 2 | `KerbClientAlloc` | `0x9EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `KerbClientFreeSupplementalCredentials` | `0x9EC0` | 35 | UnwindData |  |
| 3 | `KerbClientAllocateStoredCred` | `0xA060` | 47 | UnwindData |  |
| 11 | `KerbClientBuildStrengthenedReplyKey` | `0xA390` | 438 | UnwindData |  |
| 18 | `KerbClientFree` | `0xABE0` | 2,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `KerbClientVerifyFastArmoredKdcReply` | `0xB790` | 3,011 | UnwindData |  |
| 5 | `KerbClientBuildEncryptedAuthData` | `0xC360` | 489 | UnwindData |  |
| 30 | `KerbClientVerifyChecksum` | `0xC550` | 1,176 | UnwindData |  |
| 14 | `KerbClientDecryptApReply` | `0xC9F0` | 1,469 | UnwindData |  |
| 21 | `KerbClientPackApReply` | `0xCFC0` | 23 | UnwindData |  |
| 12 | `KerbClientBuildTicketArmorKey` | `0xD7A0` | 418 | UnwindData |  |
| 26 | `KerbClientTransformStoredCred` | `0xDFE0` | 328 | UnwindData |  |
| 9 | `KerbClientBuildKerbPriv` | `0xFA50` | 422 | UnwindData |  |
| 24 | `KerbClientSharedCleanup` | `0xFC00` | 116 | UnwindData |  |
| 25 | `KerbClientSharedInit` | `0xFC80` | 160 | UnwindData |  |
| 35 | `KerbClientVerifyPrivMessage` | `0xFD30` | 572 | UnwindData |  |
| 10 | `KerbClientBuildKeyList` | `0x104F0` | 2,836 | UnwindData |  |
| 6 | `KerbClientBuildExplicitArmorKey` | `0x110F0` | 309 | UnwindData |  |
| 7 | `KerbClientBuildFastArmoredKdcRequest` | `0x11230` | 1,402 | UnwindData |  |
| 8 | `KerbClientBuildFastChallenge` | `0x117B0` | 712 | UnwindData |  |
| 16 | `KerbClientDeriveFastChallengeKey` | `0x11A80` | 50 | UnwindData |  |
| 31 | `KerbClientVerifyEncryptedChallengePaData` | `0x11AC0` | 529 | UnwindData |  |
| 33 | `KerbClientVerifyFastArmoredKerbError` | `0x11CE0` | 1,337 | UnwindData |  |
| 34 | `KerbClientVerifyFastArmoredTgsReply` | `0x12220` | 251 | UnwindData |  |
| 4 | `KerbClientBuildAsReqAuthenticator` | `0x125D0` | 621 | UnwindData |  |
| 15 | `KerbClientDecryptPacCredentials` | `0x149D0` | 369 | UnwindData |  |
| 23 | `KerbClientParseKeyListReplyPaData` | `0x14EA0` | 487 | UnwindData |  |
| 28 | `KerbClientUnpackKdcReplyBody` | `0x15090` | 1,147 | UnwindData |  |
| 1 | `KerbClient3961UpdateSharedConfiguration` | `0x18240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `KerbClientUpdateSharedConfiguration` | `0x18260` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `KerbGetFlagsForKdcReply` | `0x18410` | 393 | UnwindData |  |
| 37 | `KerbKdcReplyContainsTgt` | `0x185A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `KerbPackKdcReplyWithEncryptedSessionKey` | `0x185E0` | 387 | UnwindData |  |
