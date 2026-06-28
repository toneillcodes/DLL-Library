# Binary Specification: puiapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\puiapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `612ce4f4cdb37b1c72cc6c7307049ed386501190cfbbf4183d45eb39fb80860b`
* **Total Exported Functions:** 52

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 49 | `DllCanUnloadNow` | `0x2BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `DllGetClassObject` | `0x2BB0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `DllRegisterServer` | `0x2C70` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `DllUnregisterServer` | `0x2C70` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `PUIAPI_CreateInstance` | `0x2D00` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PUIAPI_GetPrinter` | `0x2DA0` | 237 | UnwindData |  |
| 4 | `PUIAPI_IWaitNotify_CreateInstance` | `0x3620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PUIAPI_IWaitNotify_RegisterTimer` | `0x3630` | 56 | UnwindData |  |
| 6 | `PUIAPI_IWaitNotify_RegisterWaitObject` | `0x3670` | 56 | UnwindData |  |
| 7 | `PUIAPI_IWaitNotify_UnregisterCookie` | `0x36B0` | 1,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `STRAPI_ConvertCase` | `0x3E10` | 151 | UnwindData |  |
| 12 | `STRAPI_CrackPrintUNCName` | `0x3EB0` | 326 | UnwindData |  |
| 13 | `STRAPI_FindAndReplace` | `0x4000` | 163 | UnwindData |  |
| 14 | `STRAPI_Format` | `0x40B0` | 34 | UnwindData |  |
| 15 | `STRAPI_FormatMsg` | `0x40E0` | 34 | UnwindData |  |
| 16 | `STRAPI_FormatMsgV` | `0x4110` | 148 | UnwindData |  |
| 17 | `STRAPI_FormatV` | `0x41B0` | 101 | UnwindData |  |
| 18 | `STRAPI_GUID2String` | `0x4220` | 111 | UnwindData |  |
| 19 | `STRAPI_GetJobStatusString` | `0x42A0` | 203 | UnwindData |  |
| 20 | `STRAPI_GetPrinterStatusString` | `0x4380` | 104 | UnwindData |  |
| 21 | `STRAPI_LoadString` | `0x43F0` | 106 | UnwindData |  |
| 22 | `STRAPI_MultiCat` | `0x4460` | 152 | UnwindData |  |
| 23 | `STRAPI_String2GUID` | `0x4500` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `STRAPI_TrimString` | `0x4530` | 163 | UnwindData |  |
| 25 | `STRAPI_XMLSafeText` | `0x45E0` | 539 | UnwindData |  |
| 26 | `STRBUF_AppendString` | `0x4810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `STRBUF_Create` | `0x4830` | 110 | UnwindData |  |
| 28 | `STRBUF_CreateBSTR` | `0x48B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `STRBUF_DeleteSubstring` | `0x48D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `STRBUF_Destroy` | `0x48F0` | 34 | UnwindData |  |
| 31 | `STRBUF_FindAndReplace` | `0x4920` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `STRBUF_Format` | `0x4940` | 47 | UnwindData |  |
| 33 | `STRBUF_InsertString` | `0x4980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `STRBUF_MultiCat` | `0x49A0` | 97 | UnwindData |  |
| 35 | `STRBUF_ToLower` | `0x4A10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `STRBUF_ToUpper` | `0x4A30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `STRBUF_TrimLeft` | `0x4A50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `STRBUF_TrimRight` | `0x4A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `STRBUF_Truncate` | `0x4A90` | 60 | UnwindData |  |
| 40 | `STRBUF_Update` | `0x4AE0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `XMLAPI_GetAttributeDouble` | `0x4FC0` | 160 | UnwindData |  |
| 42 | `XMLAPI_GetAttributeLong` | `0x5070` | 160 | UnwindData |  |
| 43 | `XMLAPI_GetAttributeString` | `0x5120` | 124 | UnwindData |  |
| 44 | `XMLAPI_GetAttributeULongLong` | `0x51B0` | 126 | UnwindData |  |
| 45 | `XMLAPI_SetAttributeDouble` | `0x5240` | 119 | UnwindData |  |
| 46 | `XMLAPI_SetAttributeLong` | `0x52C0` | 163 | UnwindData |  |
| 47 | `XMLAPI_SetAttributeString` | `0x5370` | 119 | UnwindData |  |
| 48 | `XMLAPI_SetAttributeULongLong` | `0x53F0` | 121 | UnwindData |  |
| 2 | `PUIAPI_GetErrorString` | `0xEBB0` | 206 | UnwindData |  |
| 8 | `PUIAPI_ShowBrowseForPrinterDialog` | `0xEC90` | 876 | UnwindData |  |
| 9 | `PUIAPI_ShowDetailsMessageBox` | `0xF010` | 195 | UnwindData |  |
| 10 | `PUIAPI_ShowDriverPackageRemovalUI` | `0xF0E0` | 213 | UnwindData |  |
