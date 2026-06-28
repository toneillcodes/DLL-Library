# Binary Specification: iscsiexe.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\iscsiexe.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `accfbb1877961ece39adcf79511f049a5d770cbb1a3a80806a5305b319f4aef2`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `ServiceMain` | `0x3240` | 181 | UnwindData |  |
| 3 | `SvchostPushServiceGlobals` | `0x3300` | 45,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `iSNSBuildRequestPacket` | `0xE6A0` | 235 | UnwindData |  |
| 5 | `iSNSGetPGTag` | `0xEB40` | 631 | UnwindData |  |
| 6 | `iSNSGetResponseErrorCode` | `0xEDC0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `iSNSParseAndDispatchServerRequest` | `0xEE30` | 436 | UnwindData |  |
| 8 | `iSNSParseGetNextResponse` | `0xEFF0` | 503 | UnwindData |  |
| 9 | `iSNSParseQueryResponse` | `0xF1F0` | 2,687 | UnwindData |  |
| 10 | `iSNSProcessESI` | `0xFC80` | 143 | UnwindData |  |
| 11 | `iSNSProcessSCN` | `0xFD20` | 253 | UnwindData |  |
| 12 | `iSNSSetupResponsePacket` | `0xFE30` | 18,240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DiscpEstablishServiceLinkage` | `0x14570` | 42,592 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
