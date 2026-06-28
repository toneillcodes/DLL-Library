# Binary Specification: polstore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\polstore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `17abcbc04b30081cff19ccea531a48c59b36cfa98fc02acbaa04e3005003797a`
* **Total Exported Functions:** 59

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 59 | `RegCreatePolicyData` | `0x10F20` | 668 | UnwindData |  |
| 58 | `RegCreateNFAData` | `0x18720` | 1,252 | UnwindData |  |
| 6 | `IPSecAssignPolicy` | `0x1F860` | 91 | UnwindData |  |
| 7 | `IPSecClearWMIStore` | `0x1FA80` | 117 | UnwindData |  |
| 8 | `IPSecClosePolicyStore` | `0x1FB00` | 399 | UnwindData |  |
| 16 | `IPSecCreateFilterData` | `0x1FCA0` | 104 | UnwindData |  |
| 17 | `IPSecCreateISAKMPData` | `0x1FD10` | 167 | UnwindData |  |
| 18 | `IPSecCreateNFAData` | `0x1FDC0` | 237 | UnwindData |  |
| 19 | `IPSecCreateNegPolData` | `0x1FEC0` | 167 | UnwindData |  |
| 20 | `IPSecCreatePolicyData` | `0x1FF70` | 168 | UnwindData |  |
| 21 | `IPSecDeleteFilterData` | `0x20020` | 199 | UnwindData |  |
| 22 | `IPSecDeleteISAKMPData` | `0x200F0` | 199 | UnwindData |  |
| 23 | `IPSecDeleteNFAData` | `0x201C0` | 112 | UnwindData |  |
| 24 | `IPSecDeleteNegPolData` | `0x20240` | 199 | UnwindData |  |
| 25 | `IPSecDeletePolicyData` | `0x20310` | 167 | UnwindData |  |
| 26 | `IPSecEnumFilterData` | `0x203C0` | 172 | UnwindData |  |
| 27 | `IPSecEnumISAKMPData` | `0x20480` | 172 | UnwindData |  |
| 28 | `IPSecEnumNFAData` | `0x20540` | 238 | UnwindData |  |
| 29 | `IPSecEnumNegPolData` | `0x20640` | 172 | UnwindData |  |
| 30 | `IPSecEnumPolicyData` | `0x20700` | 172 | UnwindData |  |
| 31 | `IPSecExportPolicies` | `0x207C0` | 180 | UnwindData |  |
| 45 | `IPSecGetAssignedPolicyData` | `0x20880` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `IPSecGetFilterData` | `0x208B0` | 208 | UnwindData |  |
| 47 | `IPSecGetISAKMPData` | `0x20990` | 208 | UnwindData |  |
| 48 | `IPSecGetNegPolData` | `0x20A70` | 208 | UnwindData |  |
| 49 | `IPSecImportPolicies` | `0x20B50` | 197 | UnwindData |  |
| 51 | `IPSecOpenPolicyStore` | `0x20C20` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `IPSecSetFilterData` | `0x20F00` | 112 | UnwindData |  |
| 53 | `IPSecSetISAKMPData` | `0x20F80` | 175 | UnwindData |  |
| 54 | `IPSecSetNFAData` | `0x21040` | 187 | UnwindData |  |
| 55 | `IPSecSetNegPolData` | `0x21110` | 175 | UnwindData |  |
| 56 | `IPSecSetPolicyData` | `0x211D0` | 172 | UnwindData |  |
| 57 | `IPSecUnassignPolicy` | `0x21290` | 70 | UnwindData |  |
| 50 | `IPSecIsDomainPolicyAssigned` | `0x21DD0` | 326 | UnwindData |  |
| 4 | `IPSecAllocPolMem` | `0x26300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `IPSecAllocPolStr` | `0x26310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `IPSecCopyAuthMethod` | `0x26320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `IPSecCopyFilterData` | `0x26330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `IPSecCopyFilterSpec` | `0x26340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `IPSecCopyISAKMPData` | `0x26350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `IPSecCopyNFAData` | `0x26360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `IPSecCopyNegPolData` | `0x26370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `IPSecCopyPolicyData` | `0x26380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `IPSecFreeFilterData` | `0x26390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `IPSecFreeFilterSpec` | `0x263A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `IPSecFreeFilterSpecs` | `0x263B0` | 73 | UnwindData |  |
| 35 | `IPSecFreeISAKMPData` | `0x26400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `IPSecFreeMulFilterData` | `0x26410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `IPSecFreeMulISAKMPData` | `0x26420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `IPSecFreeMulNFAData` | `0x26430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `IPSecFreeMulNegPolData` | `0x26440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `IPSecFreeMulPolicyData` | `0x26450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `IPSecFreeNFAData` | `0x26460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `IPSecFreeNegPolData` | `0x26470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `IPSecFreePolStr` | `0x26480` | 27 | UnwindData |  |
| 44 | `IPSecFreePolicyData` | `0x264B0` | 18,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `GenerateIPSECPolicy` | `0x2ADB0` | 579 | UnwindData |  |
| 2 | `ProcessIPSECPolicyEx` | `0x2B190` | 1,668 | UnwindData |  |
| 3 | `WriteDirectoryPolicyToWMI` | `0x2C110` | 270 | UnwindData |  |
