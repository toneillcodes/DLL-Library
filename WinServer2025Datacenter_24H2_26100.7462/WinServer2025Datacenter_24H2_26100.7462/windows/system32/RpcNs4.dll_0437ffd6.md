# Binary Specification: RpcNs4.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\RpcNs4.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0437ffd643eb464aba1502f4ca30a6a3490c3da57a7569b54049e12c28d34675`
* **Total Exported Functions:** 62

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `RpcIfIdVectorFree` | `0x0` | - | Forwarded | Forwarded to: `RPCRT4.RpcIfIdVectorFree` |
| 7 | `RpcNsBindingExportA` | `0x1280` | 17 | UnwindData |  |
| 20 | `RpcNsBindingUnexportA` | `0x1280` | 17 | UnwindData |  |
| 1 | `I_RpcNsGetBuffer` | `0x12A0` | 20 | UnwindData |  |
| 2 | `I_RpcNsNegotiateTransferSyntax` | `0x12A0` | 20 | UnwindData |  |
| 4 | `I_RpcNsSendReceive` | `0x12A0` | 20 | UnwindData |  |
| 5 | `I_RpcReBindBuffer` | `0x12A0` | 20 | UnwindData |  |
| 8 | `RpcNsBindingExportPnPA` | `0x12A0` | 20 | UnwindData |  |
| 9 | `RpcNsBindingExportPnPW` | `0x12A0` | 20 | UnwindData |  |
| 10 | `RpcNsBindingExportW` | `0x12A0` | 20 | UnwindData |  |
| 11 | `RpcNsBindingImportBeginA` | `0x12A0` | 20 | UnwindData |  |
| 12 | `RpcNsBindingImportBeginW` | `0x12A0` | 20 | UnwindData |  |
| 13 | `RpcNsBindingImportDone` | `0x12A0` | 20 | UnwindData |  |
| 14 | `RpcNsBindingImportNext` | `0x12A0` | 20 | UnwindData |  |
| 15 | `RpcNsBindingLookupBeginA` | `0x12A0` | 20 | UnwindData |  |
| 16 | `RpcNsBindingLookupBeginW` | `0x12A0` | 20 | UnwindData |  |
| 17 | `RpcNsBindingLookupDone` | `0x12A0` | 20 | UnwindData |  |
| 18 | `RpcNsBindingLookupNext` | `0x12A0` | 20 | UnwindData |  |
| 19 | `RpcNsBindingSelect` | `0x12A0` | 20 | UnwindData |  |
| 21 | `RpcNsBindingUnexportPnPA` | `0x12A0` | 20 | UnwindData |  |
| 22 | `RpcNsBindingUnexportPnPW` | `0x12A0` | 20 | UnwindData |  |
| 23 | `RpcNsBindingUnexportW` | `0x12A0` | 20 | UnwindData |  |
| 24 | `RpcNsEntryExpandNameA` | `0x12A0` | 20 | UnwindData |  |
| 25 | `RpcNsEntryExpandNameW` | `0x12A0` | 20 | UnwindData |  |
| 26 | `RpcNsEntryObjectInqBeginA` | `0x12A0` | 20 | UnwindData |  |
| 27 | `RpcNsEntryObjectInqBeginW` | `0x12A0` | 20 | UnwindData |  |
| 28 | `RpcNsEntryObjectInqDone` | `0x12A0` | 20 | UnwindData |  |
| 29 | `RpcNsEntryObjectInqNext` | `0x12A0` | 20 | UnwindData |  |
| 30 | `RpcNsGroupDeleteA` | `0x12A0` | 20 | UnwindData |  |
| 31 | `RpcNsGroupDeleteW` | `0x12A0` | 20 | UnwindData |  |
| 32 | `RpcNsGroupMbrAddA` | `0x12A0` | 20 | UnwindData |  |
| 33 | `RpcNsGroupMbrAddW` | `0x12A0` | 20 | UnwindData |  |
| 34 | `RpcNsGroupMbrInqBeginA` | `0x12A0` | 20 | UnwindData |  |
| 35 | `RpcNsGroupMbrInqBeginW` | `0x12A0` | 20 | UnwindData |  |
| 36 | `RpcNsGroupMbrInqDone` | `0x12A0` | 20 | UnwindData |  |
| 37 | `RpcNsGroupMbrInqNextA` | `0x12A0` | 20 | UnwindData |  |
| 38 | `RpcNsGroupMbrInqNextW` | `0x12A0` | 20 | UnwindData |  |
| 39 | `RpcNsGroupMbrRemoveA` | `0x12A0` | 20 | UnwindData |  |
| 40 | `RpcNsGroupMbrRemoveW` | `0x12A0` | 20 | UnwindData |  |
| 41 | `RpcNsMgmtBindingUnexportA` | `0x12A0` | 20 | UnwindData |  |
| 42 | `RpcNsMgmtBindingUnexportW` | `0x12A0` | 20 | UnwindData |  |
| 43 | `RpcNsMgmtEntryCreateA` | `0x12A0` | 20 | UnwindData |  |
| 44 | `RpcNsMgmtEntryCreateW` | `0x12A0` | 20 | UnwindData |  |
| 45 | `RpcNsMgmtEntryDeleteA` | `0x12A0` | 20 | UnwindData |  |
| 46 | `RpcNsMgmtEntryDeleteW` | `0x12A0` | 20 | UnwindData |  |
| 47 | `RpcNsMgmtEntryInqIfIdsA` | `0x12A0` | 20 | UnwindData |  |
| 48 | `RpcNsMgmtEntryInqIfIdsW` | `0x12A0` | 20 | UnwindData |  |
| 49 | `RpcNsMgmtHandleSetExpAge` | `0x12A0` | 20 | UnwindData |  |
| 50 | `RpcNsMgmtInqExpAge` | `0x12A0` | 20 | UnwindData |  |
| 51 | `RpcNsMgmtSetExpAge` | `0x12A0` | 20 | UnwindData |  |
| 52 | `RpcNsProfileDeleteA` | `0x12A0` | 20 | UnwindData |  |
| 53 | `RpcNsProfileDeleteW` | `0x12A0` | 20 | UnwindData |  |
| 54 | `RpcNsProfileEltAddA` | `0x12A0` | 20 | UnwindData |  |
| 55 | `RpcNsProfileEltAddW` | `0x12A0` | 20 | UnwindData |  |
| 56 | `RpcNsProfileEltInqBeginA` | `0x12A0` | 20 | UnwindData |  |
| 57 | `RpcNsProfileEltInqBeginW` | `0x12A0` | 20 | UnwindData |  |
| 58 | `RpcNsProfileEltInqDone` | `0x12A0` | 20 | UnwindData |  |
| 59 | `RpcNsProfileEltInqNextA` | `0x12A0` | 20 | UnwindData |  |
| 60 | `RpcNsProfileEltInqNextW` | `0x12A0` | 20 | UnwindData |  |
| 61 | `RpcNsProfileEltRemoveA` | `0x12A0` | 20 | UnwindData |  |
| 62 | `RpcNsProfileEltRemoveW` | `0x12A0` | 20 | UnwindData |  |
| 3 | `I_RpcNsRaiseException` | `0x12C0` | 0 | Indeterminate |  |
