# Binary Specification: mscat32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mscat32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2bc0c6ecbdc49f8ab934a921f82a3ec8112be17208432a0122b86496032c68dd`
* **Total Exported Functions:** 36

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `CatalogCompactHashDatabase` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CatalogCompactHashDatabase` |
| 3 | `CryptCATAdminAcquireContext` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATAdminAcquireContext` |
| 4 | `CryptCATAdminAddCatalog` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATAdminAddCatalog` |
| 5 | `CryptCATAdminCalcHashFromFileHandle` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATAdminCalcHashFromFileHandle` |
| 6 | `CryptCATAdminEnumCatalogFromHash` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATAdminEnumCatalogFromHash` |
| 7 | `CryptCATAdminReleaseCatalogContext` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATAdminReleaseCatalogContext` |
| 8 | `CryptCATAdminReleaseContext` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATAdminReleaseContext` |
| 9 | `CryptCATCDFClose` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATCDFClose` |
| 10 | `CryptCATCDFEnumAttributes` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATCDFEnumAttributes` |
| 11 | `CryptCATCDFEnumAttributesWithCDFTag` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATCDFEnumAttributesWithCDFTag` |
| 12 | `CryptCATCDFEnumCatAttributes` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATCDFEnumCatAttributes` |
| 13 | `CryptCATCDFEnumMembers` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATCDFEnumMembers` |
| 14 | `CryptCATCDFEnumMembersByCDFTag` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATCDFEnumMembersByCDFTag` |
| 15 | `CryptCATCDFEnumMembersByCDFTagEx` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATCDFEnumMembersByCDFTagEx` |
| 16 | `CryptCATCDFOpen` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATCDFOpen` |
| 17 | `CryptCATCatalogInfoFromContext` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATCatalogInfoFromContext` |
| 18 | `CryptCATClose` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATClose` |
| 19 | `CryptCATEnumerateAttr` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATEnumerateAttr` |
| 20 | `CryptCATEnumerateCatAttr` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATEnumerateCatAttr` |
| 21 | `CryptCATEnumerateMember` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATEnumerateMember` |
| 22 | `CryptCATGetAttrInfo` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATGetAttrInfo` |
| 23 | `CryptCATGetCatAttrInfo` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATGetCatAttrInfo` |
| 24 | `CryptCATGetMemberInfo` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATGetMemberInfo` |
| 25 | `CryptCATHandleFromStore` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATHandleFromStore` |
| 26 | `CryptCATOpen` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATOpen` |
| 27 | `CryptCATPersistStore` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATPersistStore` |
| 28 | `CryptCATPutAttrInfo` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATPutAttrInfo` |
| 29 | `CryptCATPutCatAttrInfo` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATPutCatAttrInfo` |
| 30 | `CryptCATPutMemberInfo` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATPutMemberInfo` |
| 31 | `CryptCATStoreFromHandle` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATStoreFromHandle` |
| 1 | `CryptCATVerifyMember` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.CryptCATVerifyMember` |
| 32 | `DllRegisterServer` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.mscat32DllRegisterServer` |
| 33 | `DllUnregisterServer` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.mscat32DllUnregisterServer` |
| 34 | `IsCatalogFile` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.IsCatalogFile` |
| 35 | `MsCatConstructHashTag` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.MsCatConstructHashTag` |
| 36 | `MsCatFreeHashTag` | `0x0` | - | Forwarded | Forwarded to: `Wintrust.MsCatFreeHashTag` |
