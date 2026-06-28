# Binary Specification: tpmvsc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\tpmvsc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `21d8cc17c3b4911a197284946119fcb0bb4ce779adbe5d811a545951762278e5`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1CBC0` | 218 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1CCA0` | 251 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1CF40` | 276 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1D060` | 235 | UnwindData |  |
| 5 | `TpmVCardCreate` | `0x31390` | 610 | UnwindData |  |
| 6 | `TpmVCardCreateInProc` | `0x31600` | 589 | UnwindData |  |
| 7 | `TpmVCardDestroy` | `0x31860` | 382 | UnwindData |  |
| 8 | `TpmVCardDestroyInProc` | `0x319F0` | 383 | UnwindData |  |
| 9 | `VCardAuthenticatePin` | `0x31B80` | 329 | UnwindData |  |
| 10 | `VCardChangePin` | `0x31CD0` | 361 | UnwindData |  |
| 11 | `VCardClose` | `0x31E40` | 373 | UnwindData |  |
| 12 | `VCardCloseChannel` | `0x31FC0` | 279 | UnwindData |  |
| 13 | `VCardCreateClaim` | `0x320E0` | 397 | UnwindData |  |
| 14 | `VCardCreateKey` | `0x32280` | 623 | UnwindData |  |
| 15 | `VCardDeauthenticate` | `0x32500` | 277 | UnwindData |  |
| 16 | `VCardDecrypt` | `0x32620` | 494 | UnwindData |  |
| 17 | `VCardDeinitialize` | `0x32820` | 366 | UnwindData |  |
| 18 | `VCardDeleteKey` | `0x329A0` | 401 | UnwindData |  |
| 19 | `VCardEncrypt` | `0x32B40` | 494 | UnwindData |  |
| 20 | `VCardExportRsaPubKey` | `0x32D40` | 347 | UnwindData |  |
| 21 | `VCardGetAikCertificate` | `0x32EB0` | 336 | UnwindData |  |
| 22 | `VCardGetAikContainerName` | `0x33010` | 329 | UnwindData |  |
| 23 | `VCardGetChallenge` | `0x33160` | 384 | UnwindData |  |
| 24 | `VCardGetKeyType` | `0x332F0` | 311 | UnwindData |  |
| 25 | `VCardGetPinLength` | `0x33430` | 322 | UnwindData |  |
| 26 | `VCardGetRemainingRetryCount` | `0x33580` | 333 | UnwindData |  |
| 27 | `VCardGetTransportKeyAlg` | `0x336E0` | 151 | UnwindData |  |
| 28 | `VCardImportRsaKey` | `0x33780` | 777 | UnwindData |  |
| 29 | `VCardImportSymKey` | `0x33A90` | 507 | UnwindData |  |
| 30 | `VCardInitialize` | `0x33CA0` | 306 | UnwindData |  |
| 31 | `VCardInvalidateChallenge` | `0x33DE0` | 310 | UnwindData |  |
| 32 | `VCardOpen` | `0x33F20` | 394 | UnwindData |  |
| 33 | `VCardOpenChannel` | `0x340B0` | 388 | UnwindData |  |
| 34 | `VCardResetPin` | `0x34240` | 329 | UnwindData |  |
| 35 | `VCardSetResponse` | `0x34390` | 379 | UnwindData |  |
| 36 | `VCardSignHash` | `0x34520` | 489 | UnwindData |  |
| 37 | `VCardUnblockPin` | `0x34710` | 331 | UnwindData |  |
