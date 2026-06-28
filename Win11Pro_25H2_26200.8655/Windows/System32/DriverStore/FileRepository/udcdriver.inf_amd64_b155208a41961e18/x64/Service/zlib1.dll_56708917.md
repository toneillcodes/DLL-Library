# Binary Specification: zlib1.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\udcdriver.inf_amd64_b155208a41961e18\x64\Service\zlib1.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `567089174ad7460e6ce93dc855e95b7a6bc7ba7a3d2732105c0a48434350a7c0`
* **Total Exported Functions:** 86

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `adler32` | `0x1000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `adler32_combine` | `0x1010` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `adler32_z` | `0x1100` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `compress` | `0x13E0` | 22 | UnwindData |  |
| 5 | `compress2` | `0x1400` | 254 | UnwindData |  |
| 6 | `compressBound` | `0x1500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `crc32` | `0x1520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `crc32_combine` | `0x1530` | 97 | UnwindData |  |
| 9 | `crc32_combine_gen` | `0x15A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `crc32_combine_op` | `0x15B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `crc32_z` | `0x15F0` | 46 | UnwindData |  |
| 27 | `get_crc_table` | `0x1AA0` | 3,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `deflate` | `0x2A10` | 126 | UnwindData |  |
| 13 | `deflateBound` | `0x3480` | 436 | UnwindData |  |
| 14 | `deflateCopy` | `0x3640` | 118 | UnwindData |  |
| 15 | `deflateEnd` | `0x3880` | 116 | UnwindData |  |
| 16 | `deflateGetDictionary` | `0x39B0` | 105 | UnwindData |  |
| 17 | `deflateInit2_` | `0x3A80` | 81 | UnwindData |  |
| 18 | `deflateInit_` | `0x3D20` | 52 | UnwindData |  |
| 19 | `deflateParams` | `0x3D60` | 455 | UnwindData |  |
| 20 | `deflatePending` | `0x3F30` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `deflatePrime` | `0x3FB0` | 112 | UnwindData |  |
| 22 | `deflateReset` | `0x40E0` | 32 | UnwindData |  |
| 23 | `deflateResetKeep` | `0x41B0` | 125 | UnwindData |  |
| 24 | `deflateSetDictionary` | `0x42B0` | 173 | UnwindData |  |
| 25 | `deflateSetHeader` | `0x4500` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `deflateTune` | `0x4570` | 3,216 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `gzclose` | `0x5200` | 1,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `gzbuffer` | `0x5710` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `gzclearerr` | `0x5750` | 16 | UnwindData |  |
| 34 | `gzdopen` | `0x57B0` | 129 | UnwindData |  |
| 35 | `gzeof` | `0x5840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `gzerror` | `0x5860` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `gzoffset` | `0x58B0` | 109 | UnwindData |  |
| 44 | `gzoffset64` | `0x5920` | 91 | UnwindData |  |
| 45 | `gzopen` | `0x5980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `gzopen64` | `0x5980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `gzopen_w` | `0x5990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `gzrewind` | `0x59A0` | 84 | UnwindData |  |
| 53 | `gzseek` | `0x5A00` | 34 | UnwindData |  |
| 54 | `gzseek64` | `0x5A30` | 451 | UnwindData |  |
| 56 | `gztell` | `0x5C00` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `gztell64` | `0x5C60` | 2,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `gzclose_r` | `0x64C0` | 35 | UnwindData |  |
| 33 | `gzdirect` | `0x6570` | 56 | UnwindData |  |
| 38 | `gzfread` | `0x65B0` | 120 | UnwindData |  |
| 40 | `gzgetc` | `0x6630` | 115 | UnwindData |  |
| 41 | `gzgetc_` | `0x66B0` | 105 | UnwindData |  |
| 42 | `gzgets` | `0x6720` | 301 | UnwindData |  |
| 51 | `gzread` | `0x6850` | 103 | UnwindData |  |
| 58 | `gzungetc` | `0x68C0` | 315 | UnwindData |  |
| 32 | `gzclose_w` | `0x7050` | 207 | UnwindData |  |
| 37 | `gzflush` | `0x7120` | 107 | UnwindData |  |
| 39 | `gzfwrite` | `0x7190` | 114 | UnwindData |  |
| 48 | `gzprintf` | `0x7210` | 34 | UnwindData |  |
| 49 | `gzputc` | `0x7240` | 202 | UnwindData |  |
| 50 | `gzputs` | `0x7310` | 33 | UnwindData |  |
| 55 | `gzsetparams` | `0x73A0` | 64 | UnwindData |  |
| 59 | `gzvprintf` | `0x74B0` | 129 | UnwindData |  |
| 60 | `gzwrite` | `0x7640` | 65 | UnwindData |  |
| 61 | `inflate` | `0x7690` | 6,292 | UnwindData |  |
| 65 | `inflateCodesUsed` | `0x8F30` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `inflateCopy` | `0x8F80` | 103 | UnwindData |  |
| 67 | `inflateEnd` | `0x9170` | 113 | UnwindData |  |
| 68 | `inflateGetDictionary` | `0x91F0` | 66 | UnwindData |  |
| 69 | `inflateGetHeader` | `0x92A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `inflateInit2_` | `0x92F0` | 69 | UnwindData |  |
| 71 | `inflateInit_` | `0x93F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `inflateMark` | `0x9400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `inflatePrime` | `0x9480` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `inflateReset` | `0x9500` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `inflateReset2` | `0x9610` | 193 | UnwindData |  |
| 76 | `inflateResetKeep` | `0x96E0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `inflateSetDictionary` | `0x97A0` | 234 | UnwindData |  |
| 78 | `inflateSync` | `0x9890` | 83 | UnwindData |  |
| 79 | `inflateSyncPoint` | `0x9A50` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `inflateUndermine` | `0x9AA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `inflateValidate` | `0x9AF0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `inflateBack` | `0x9CD0` | 63 | UnwindData |  |
| 63 | `inflateBackEnd` | `0xACA0` | 65 | UnwindData |  |
| 64 | `inflateBackInit_` | `0xACF0` | 87 | UnwindData |  |
| 82 | `uncompress` | `0xD580` | 24 | UnwindData |  |
| 83 | `uncompress2` | `0xD5A0` | 121 | UnwindData |  |
| 84 | `zError` | `0xD700` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `zlibCompileFlags` | `0xD750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `zlibVersion` | `0xD760` | 184 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
