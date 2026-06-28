# Binary Specification: puiapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\puiapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c9bd477693aa74d9a7332af2ecfebb19b14e012f8fa8fcc9cdf50fa54dfe955c`
* **Total Exported Functions:** 52

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 49 | `DllCanUnloadNow` | `0x2B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `DllGetClassObject` | `0x2B60` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `DllRegisterServer` | `0x2C20` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `DllUnregisterServer` | `0x2C20` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `PUIAPI_CreateInstance` | `0x2CB0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `PUIAPI_GetPrinter` | `0x2D50` | 237 | UnwindData |  |
| 4 | `PUIAPI_IWaitNotify_CreateInstance` | `0x35D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `PUIAPI_IWaitNotify_RegisterTimer` | `0x35E0` | 56 | UnwindData |  |
| 6 | `PUIAPI_IWaitNotify_RegisterWaitObject` | `0x3620` | 56 | UnwindData |  |
| 7 | `PUIAPI_IWaitNotify_UnregisterCookie` | `0x3660` | 1,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `STRAPI_ConvertCase` | `0x3DC0` | 151 | UnwindData |  |
| 12 | `STRAPI_CrackPrintUNCName` | `0x3E60` | 326 | UnwindData |  |
| 13 | `STRAPI_FindAndReplace` | `0x3FB0` | 163 | UnwindData |  |
| 14 | `STRAPI_Format` | `0x4060` | 34 | UnwindData |  |
| 15 | `STRAPI_FormatMsg` | `0x4090` | 34 | UnwindData |  |
| 16 | `STRAPI_FormatMsgV` | `0x40C0` | 148 | UnwindData |  |
| 17 | `STRAPI_FormatV` | `0x4160` | 101 | UnwindData |  |
| 18 | `STRAPI_GUID2String` | `0x41D0` | 111 | UnwindData |  |
| 19 | `STRAPI_GetJobStatusString` | `0x4250` | 203 | UnwindData |  |
| 20 | `STRAPI_GetPrinterStatusString` | `0x4330` | 104 | UnwindData |  |
| 21 | `STRAPI_LoadString` | `0x43A0` | 106 | UnwindData |  |
| 22 | `STRAPI_MultiCat` | `0x4410` | 152 | UnwindData |  |
| 23 | `STRAPI_String2GUID` | `0x44B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `STRAPI_TrimString` | `0x44E0` | 163 | UnwindData |  |
| 25 | `STRAPI_XMLSafeText` | `0x4590` | 539 | UnwindData |  |
| 26 | `STRBUF_AppendString` | `0x47C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `STRBUF_Create` | `0x47E0` | 110 | UnwindData |  |
| 28 | `STRBUF_CreateBSTR` | `0x4860` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `STRBUF_DeleteSubstring` | `0x4880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `STRBUF_Destroy` | `0x48A0` | 34 | UnwindData |  |
| 31 | `STRBUF_FindAndReplace` | `0x48D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `STRBUF_Format` | `0x48F0` | 47 | UnwindData |  |
| 33 | `STRBUF_InsertString` | `0x4930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `STRBUF_MultiCat` | `0x4950` | 97 | UnwindData |  |
| 35 | `STRBUF_ToLower` | `0x49C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `STRBUF_ToUpper` | `0x49E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `STRBUF_TrimLeft` | `0x4A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `STRBUF_TrimRight` | `0x4A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `STRBUF_Truncate` | `0x4A40` | 60 | UnwindData |  |
| 40 | `STRBUF_Update` | `0x4A90` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `XMLAPI_GetAttributeDouble` | `0x4F70` | 160 | UnwindData |  |
| 42 | `XMLAPI_GetAttributeLong` | `0x5020` | 160 | UnwindData |  |
| 43 | `XMLAPI_GetAttributeString` | `0x50D0` | 124 | UnwindData |  |
| 44 | `XMLAPI_GetAttributeULongLong` | `0x5160` | 126 | UnwindData |  |
| 45 | `XMLAPI_SetAttributeDouble` | `0x51F0` | 119 | UnwindData |  |
| 46 | `XMLAPI_SetAttributeLong` | `0x5270` | 163 | UnwindData |  |
| 47 | `XMLAPI_SetAttributeString` | `0x5320` | 119 | UnwindData |  |
| 48 | `XMLAPI_SetAttributeULongLong` | `0x53A0` | 121 | UnwindData |  |
| 2 | `PUIAPI_GetErrorString` | `0xEB60` | 206 | UnwindData |  |
| 8 | `PUIAPI_ShowBrowseForPrinterDialog` | `0xEC40` | 876 | UnwindData |  |
| 9 | `PUIAPI_ShowDetailsMessageBox` | `0xEFC0` | 195 | UnwindData |  |
| 10 | `PUIAPI_ShowDriverPackageRemovalUI` | `0xF090` | 213 | UnwindData |  |
