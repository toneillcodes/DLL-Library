# Binary Specification: bz2.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Service\bz2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ea37f71c9537320e2c3b7ed688a977fe41db9aee78bfd9508fe63e5ca31e362b`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `BZ2_bzBuffToBuffCompress` | `0xAF50` | 628 | UnwindData |  |
| 2 | `BZ2_bzBuffToBuffDecompress` | `0xB1D0` | 574 | UnwindData |  |
| 3 | `BZ2_bzCompress` | `0xB410` | 362 | UnwindData |  |
| 4 | `BZ2_bzCompressEnd` | `0xB580` | 128 | UnwindData |  |
| 5 | `BZ2_bzCompressInit` | `0xB600` | 60 | UnwindData |  |
| 6 | `BZ2_bzDecompress` | `0xB900` | 49 | UnwindData |  |
| 7 | `BZ2_bzDecompressEnd` | `0xBAC0` | 137 | UnwindData |  |
| 8 | `BZ2_bzDecompressInit` | `0xBB50` | 257 | UnwindData |  |
| 9 | `BZ2_bzRead` | `0xBC60` | 155 | UnwindData |  |
| 10 | `BZ2_bzReadClose` | `0xBEB0` | 112 | UnwindData |  |
| 11 | `BZ2_bzReadGetUnused` | `0xBF20` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `BZ2_bzReadOpen` | `0xBFA0` | 376 | UnwindData |  |
| 13 | `BZ2_bzWrite` | `0xC120` | 109 | UnwindData |  |
| 14 | `BZ2_bzWriteClose` | `0xC310` | 146 | UnwindData |  |
| 15 | `BZ2_bzWriteClose64` | `0xC5B0` | 146 | UnwindData |  |
| 16 | `BZ2_bzWriteOpen` | `0xC8A0` | 347 | UnwindData |  |
| 17 | `BZ2_bzclose` | `0xCA70` | 24 | UnwindData |  |
| 18 | `BZ2_bzdopen` | `0xCD00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `BZ2_bzerror` | `0xCD20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `BZ2_bzflush` | `0xCD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `BZ2_bzlibVersion` | `0xCD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `BZ2_bzopen` | `0xCD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `BZ2_bzread` | `0xCD80` | 431 | UnwindData |  |
| 24 | `BZ2_bzwrite` | `0xCF30` | 455 | UnwindData |  |
