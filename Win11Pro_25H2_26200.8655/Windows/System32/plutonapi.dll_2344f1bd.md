# Binary Specification: plutonapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\plutonapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2344f1bdeda50c9718a866047e1f5491aa32f221366eaa8d59b681317c778438`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `PlutonAttestation_GetLeafCert` | `0x6850` | 289 | UnwindData |  |
| 26 | `PlutonPlayReady_SendReceiveData` | `0x6980` | 289 | UnwindData |  |
| 2 | `PlutonFree` | `0x6E40` | 62 | UnwindData |  |
| 27 | `PlutonQuery_ColdLoadDeviceInfo` | `0x7250` | 491 | UnwindData |  |
| 28 | `PlutonQuery_DevicePresent` | `0x7450` | 522 | UnwindData |  |
| 29 | `PlutonQuery_EnumeratePcbiVersions` | `0x7660` | 657 | UnwindData |  |
| 30 | `PlutonQuery_EnumerateServices` | `0x7900` | 699 | UnwindData |  |
| 31 | `PlutonQuery_FirmwareLoaded` | `0x7BD0` | 523 | UnwindData |  |
| 32 | `PlutonQuery_GetEKICACertificate` | `0x7DF0` | 145 | UnwindData |  |
| 33 | `PlutonQuery_GetPackageInfo` | `0x7E90` | 517 | UnwindData |  |
| 34 | `PlutonQuery_HotLoadDeviceInfo` | `0x80A0` | 491 | UnwindData |  |
| 3 | `PlutonKsp_ActivateRsaAik` | `0x117A0` | 22 | UnwindData |  |
| 4 | `PlutonKsp_AesDecrypt` | `0x117C0` | 2,910 | UnwindData |  |
| 5 | `PlutonKsp_AesEncrypt` | `0x12330` | 2,912 | UnwindData |  |
| 6 | `PlutonKsp_CertifyRsaKey` | `0x12EA0` | 22 | UnwindData |  |
| 7 | `PlutonKsp_CreateAesKey` | `0x12EC0` | 1,896 | UnwindData |  |
| 8 | `PlutonKsp_CreateHmacKey` | `0x13630` | 22 | UnwindData |  |
| 9 | `PlutonKsp_CreateRsaKeyPair` | `0x13650` | 1,627 | UnwindData |  |
| 10 | `PlutonKsp_DeriveAesKey` | `0x13CC0` | 3,284 | UnwindData |  |
| 11 | `PlutonKsp_DeriveHmacKey` | `0x149A0` | 3,111 | UnwindData |  |
| 12 | `PlutonKsp_GetAesPublicContext` | `0x155D0` | 515 | UnwindData |  |
| 13 | `PlutonKsp_GetEccEkCert` | `0x157E0` | 22 | UnwindData |  |
| 14 | `PlutonKsp_GetEccEkPub` | `0x15800` | 22 | UnwindData |  |
| 15 | `PlutonKsp_GetHmacPublicContext` | `0x15820` | 515 | UnwindData |  |
| 16 | `PlutonKsp_GetKspFirmwareVersion` | `0x15A30` | 577 | UnwindData |  |
| 17 | `PlutonKsp_GetRsaEkCert` | `0x15C80` | 22 | UnwindData |  |
| 18 | `PlutonKsp_GetRsaEkPub` | `0x15CA0` | 22 | UnwindData |  |
| 19 | `PlutonKsp_GetRsaPublicContext` | `0x15CC0` | 519 | UnwindData |  |
| 20 | `PlutonKsp_HmacSignData` | `0x15ED0` | 3,208 | UnwindData |  |
| 21 | `PlutonKsp_ImportHmacKey` | `0x16B60` | 2,575 | UnwindData |  |
| 22 | `PlutonKsp_RsaAttestKey` | `0x17580` | 22 | UnwindData |  |
| 23 | `PlutonKsp_RsaDecrypt` | `0x175A0` | 2,735 | UnwindData |  |
| 24 | `PlutonKsp_RsaSignHash` | `0x18060` | 2,623 | UnwindData |  |
| 25 | `PlutonKsp_SetOsSecret` | `0x18AB0` | 934 | UnwindData |  |
