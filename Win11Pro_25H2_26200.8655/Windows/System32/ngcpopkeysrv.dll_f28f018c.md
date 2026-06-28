# Binary Specification: ngcpopkeysrv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ngcpopkeysrv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f28f018c91b30471ed2b2a3592ba4bf27f8f92acdfe8357ac61c855c1dc78896`
* **Total Exported Functions:** 20

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `s_NgcCreateTokenBindingAik` | `0x11C40` | 352 | UnwindData |  |
| 5 | `s_NgcDecryptWithSymmetricGcmPopKey` | `0x11DB0` | 507 | UnwindData |  |
| 6 | `s_NgcDecryptWithSymmetricPopKey` | `0x11FC0` | 421 | UnwindData |  |
| 7 | `s_NgcDeleteSymmetricPopKeyTransportKey` | `0x12170` | 269 | UnwindData |  |
| 8 | `s_NgcDeleteTokenBindingAik` | `0x12290` | 271 | UnwindData |  |
| 9 | `s_NgcEncryptWithSymmetricGcmPopKey` | `0x123B0` | 507 | UnwindData |  |
| 10 | `s_NgcEncryptWithSymmetricPopKey` | `0x125C0` | 421 | UnwindData |  |
| 11 | `s_NgcGetKeyAttestationForContainerService` | `0x12770` | 343 | UnwindData |  |
| 14 | `s_NgcGetSymmetricPopKeyTransportKey` | `0x128D0` | 186 | UnwindData |  |
| 15 | `s_NgcGetSymmetricPopKeyTransportKeyName` | `0x12990` | 114 | UnwindData |  |
| 16 | `s_NgcGetTokenBindingAikName` | `0x12F70` | 301 | UnwindData |  |
| 17 | `s_NgcImportSymmetricPopKey` | `0x130B0` | 328 | UnwindData |  |
| 18 | `s_NgcRenewKeyAttestation` | `0x13200` | 272 | UnwindData |  |
| 19 | `s_NgcSignWithSymmetricPopKey` | `0x13320` | 387 | UnwindData |  |
| 20 | `s_NgcVerifyWithSymmetricPopKey` | `0x134B0` | 379 | UnwindData |  |
| 1 | `NgcGetPregenKey` | `0x20A00` | 270 | UnwindData |  |
| 2 | `NgcPregenKey` | `0x20B20` | 257 | UnwindData |  |
| 3 | `NgcTriggerTask` | `0x20C30` | 253 | UnwindData |  |
| 12 | `s_NgcGetPregenKeyState` | `0x20D40` | 270 | UnwindData |  |
| 13 | `s_NgcGetPregenUserKey` | `0x20E60` | 390 | UnwindData |  |
