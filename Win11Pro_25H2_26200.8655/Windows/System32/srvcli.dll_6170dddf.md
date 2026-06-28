# Binary Specification: srvcli.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\srvcli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6170dddf6a03b2b3e9520e301fb3a06fae7fb4c617b2c7d7cceb2160e829fd4d`
* **Total Exported Functions:** 67

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 60 | `NetShareGetInfo` | `0x1CD0` | 755 | UnwindData |  |
| 58 | `NetShareEnum` | `0x1FD0` | 894 | UnwindData |  |
| 49 | `NetServerTransportEnum` | `0x24F0` | 374 | UnwindData |  |
| 43 | `NetServerGetInfo` | `0x2670` | 305 | UnwindData |  |
| 3 | `I_NetServerSetServiceBitsEx` | `0x32A0` | 219 | UnwindData |  |
| 51 | `NetSessionEnum` | `0x34C0` | 410 | UnwindData |  |
| 1 | `I_NetDfsGetVersion` | `0x4C30` | 190 | UnwindData |  |
| 2 | `I_NetServerSetServiceBits` | `0x5100` | 255 | UnwindData |  |
| 4 | `LocalAliasGet` | `0x5210` | 197 | UnwindData |  |
| 5 | `LocalFileClose` | `0x52E0` | 190 | UnwindData |  |
| 6 | `LocalFileEnum` | `0x53B0` | 90 | UnwindData |  |
| 7 | `LocalFileEnumEx` | `0x5410` | 411 | UnwindData |  |
| 8 | `LocalFileGetInfo` | `0x55C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `LocalFileGetInfoEx` | `0x55E0` | 233 | UnwindData |  |
| 10 | `LocalServerAlternativePortEnum` | `0x56D0` | 194 | UnwindData |  |
| 11 | `LocalServerAlternativePortUpdate` | `0x57A0` | 194 | UnwindData |  |
| 12 | `LocalServerCertificateMappingAceAdd` | `0x5870` | 223 | UnwindData |  |
| 13 | `LocalServerCertificateMappingAceRemove` | `0x5960` | 223 | UnwindData |  |
| 14 | `LocalServerCertificateMappingAdd` | `0x5A50` | 205 | UnwindData |  |
| 15 | `LocalServerCertificateMappingEnum` | `0x5B30` | 239 | UnwindData |  |
| 16 | `LocalServerCertificateMappingGet` | `0x5C30` | 283 | UnwindData |  |
| 17 | `LocalServerCertificateMappingModify` | `0x5D60` | 201 | UnwindData |  |
| 18 | `LocalServerCertificateMappingRemove` | `0x5E30` | 201 | UnwindData |  |
| 19 | `LocalServerSmbDirectModuleControl` | `0x5F00` | 187 | UnwindData |  |
| 20 | `LocalSessionDel` | `0x5FD0` | 190 | UnwindData |  |
| 21 | `LocalSessionEnum` | `0x60A0` | 78 | UnwindData |  |
| 22 | `LocalSessionEnumEx` | `0x6100` | 400 | UnwindData |  |
| 23 | `LocalSessionGetInfo` | `0x62A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `LocalSessionGetInfoEx` | `0x62C0` | 233 | UnwindData |  |
| 25 | `LocalShareAdd` | `0x63B0` | 587 | UnwindData |  |
| 26 | `LocalShareDelEx` | `0x6610` | 197 | UnwindData |  |
| 27 | `LocalShareEnum` | `0x66E0` | 31 | UnwindData |  |
| 28 | `LocalShareEnumEx` | `0x6710` | 323 | UnwindData |  |
| 29 | `LocalShareGetInfo` | `0x6860` | 31 | UnwindData |  |
| 30 | `LocalShareGetInfoEx` | `0x6890` | 250 | UnwindData |  |
| 31 | `LocalShareSetInfo` | `0x6990` | 542 | UnwindData |  |
| 32 | `NetConnectionEnum` | `0x6BC0` | 401 | UnwindData |  |
| 33 | `NetFileClose` | `0x6D60` | 187 | UnwindData |  |
| 34 | `NetFileEnum` | `0x6E30` | 403 | UnwindData |  |
| 35 | `NetFileGetInfo` | `0x6FD0` | 266 | UnwindData |  |
| 36 | `NetRemoteTOD` | `0x70E0` | 220 | UnwindData |  |
| 37 | `NetServerAliasAdd` | `0x71D0` | 226 | UnwindData |  |
| 38 | `NetServerAliasDel` | `0x72C0` | 216 | UnwindData |  |
| 39 | `NetServerAliasEnum` | `0x73A0` | 440 | UnwindData |  |
| 40 | `NetServerComputerNameAdd` | `0x7560` | 710 | UnwindData |  |
| 41 | `NetServerComputerNameDel` | `0x7830` | 414 | UnwindData |  |
| 42 | `NetServerDiskEnum` | `0x79E0` | 368 | UnwindData |  |
| 44 | `NetServerSetInfo` | `0x7B60` | 233 | UnwindData |  |
| 45 | `NetServerStatisticsGet` | `0x7C50` | 278 | UnwindData |  |
| 46 | `NetServerTransportAdd` | `0x7D70` | 201 | UnwindData |  |
| 47 | `NetServerTransportAddEx` | `0x7E40` | 214 | UnwindData |  |
| 48 | `NetServerTransportDel` | `0x7F20` | 219 | UnwindData |  |
| 50 | `NetSessionDel` | `0x8120` | 204 | UnwindData |  |
| 52 | `NetSessionGetInfo` | `0x8200` | 343 | UnwindData |  |
| 53 | `NetShareAdd` | `0x8360` | 721 | UnwindData |  |
| 54 | `NetShareCheck` | `0x8640` | 239 | UnwindData |  |
| 55 | `NetShareDel` | `0x8740` | 451 | UnwindData |  |
| 56 | `NetShareDelEx` | `0x8910` | 386 | UnwindData |  |
| 57 | `NetShareDelSticky` | `0x8AA0` | 239 | UnwindData |  |
| 59 | `NetShareEnumSticky` | `0x8BA0` | 546 | UnwindData |  |
| 61 | `NetShareSetInfo` | `0x8DD0` | 789 | UnwindData |  |
| 62 | `NetpsNameCanonicalize` | `0x90F0` | 258 | UnwindData |  |
| 63 | `NetpsNameCompare` | `0x9200` | 247 | UnwindData |  |
| 64 | `NetpsNameValidate` | `0x9300` | 236 | UnwindData |  |
| 65 | `NetpsPathCanonicalize` | `0x9400` | 273 | UnwindData |  |
| 66 | `NetpsPathCompare` | `0x9520` | 247 | UnwindData |  |
| 67 | `NetpsPathType` | `0x9620` | 236 | UnwindData |  |
