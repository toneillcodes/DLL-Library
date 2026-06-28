# Binary Specification: windows.storage.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\windows.storage.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3d003d75c1be1ee6878472948ac0a123cc1517cb6516847ac2d44c690601485a`
* **Total Exported Functions:** 692

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 459 | `SHGetFolderPathW` | `0x1CCE0` | 32 | UnwindData |  |
| 458 | `SHGetFolderPathEx` | `0x1CFA0` | 21 | UnwindData |  |
| 466 | `SHGetKnownFolderIDList_Internal` | `0x1EA10` | 890 | UnwindData |  |
| 465 | `SHGetKnownFolderIDList` | `0x20080` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `SHGetKnownFolderItem` | `0x203C0` | 117 | UnwindData |  |
| 332 | `NeverProvidedByJunction` | `0x22B10` | 9,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `DeserializeTextToLink` | `0x25020` | 268 | UnwindData |  |
| 472 | `SHGetNameFromIDList` | `0x259F0` | 126 | UnwindData |  |
| 590 | `ShellExecuteExW` | `0x2AAC0` | 255 | UnwindData |  |
| 393 | `SHBindWithFolder2Shim` | `0x2DCC0` | 186 | UnwindData |  |
| 424 | `SHCreateShellItemArrayFromDataObject` | `0x30210` | 250 | UnwindData |  |
| 293 | `ILIsParent` | `0x34310` | 25 | UnwindData |  |
| 575 | `SendNotificationsForLibraryItem` | `0x35440` | 244 | UnwindData |  |
| 4 | `SHChangeNotifyDeregister` | `0x3F160` | 260 | UnwindData |  |
| 2 | `SHChangeNotifyRegister` | `0x3F3D0` | 399 | UnwindData |  |
| 460 | `SHGetIDListFromObject` | `0x48010` | 164 | UnwindData |  |
| 279 | `ILClone` | `0x49240` | 39 | UnwindData |  |
| 512 | `SHQueryShellFolderValue` | `0x4BEA0` | 765 | UnwindData |  |
| 297 | `IUnknown_GetFolderTargetIDList` | `0x4FBB0` | 428 | UnwindData |  |
| 421 | `SHCreateSessionKey` | `0x52CD0` | 151 | UnwindData |  |
| 15 | `GetCurrentSessionId` | `0x52D70` | 78 | UnwindData |  |
| 486 | `SHGetSpecialFolderPathW` | `0x53CF0` | 540 | UnwindData |  |
| 479 | `SHGetPathFromIDListEx` | `0x57080` | 1,161 | UnwindData |  |
| 388 | `SHBindToFolderIDListParentEx` | `0x576C0` | 3,150 | UnwindData |  |
| 392 | `SHBindToParent` | `0x58E20` | 1,498 | UnwindData |  |
| 105 | `CDesktopFolder_CreateInstanceWithBindContext` | `0x5C830` | 2,621 | UnwindData |  |
| 506 | `SHParseDisplayName` | `0x5D380` | 713 | UnwindData |  |
| 292 | `ILIsEqual` | `0x5D7B0` | 371 | UnwindData |  |
| 862 | *Ordinal Only* | `0x5D930` | 394 | UnwindData |  |
| 448 | `SHGetDesktopFolder` | `0x5DAC0` | 1,879 | UnwindData |  |
| 134 | `CShellItemArrayWithCommonParent_CreateInstance` | `0x6B270` | 203 | UnwindData |  |
| 423 | `SHCreateShellItemArray` | `0x6B690` | 328 | UnwindData |  |
| 132 | `CShellItemArrayAsCollection_CreateInstance` | `0x6B7E0` | 203 | UnwindData |  |
| 8 | `CreateShellItemArrayFromAliasNamespaces` | `0x6D6C0` | 612 | UnwindData |  |
| 866 | *Ordinal Only* | `0x6F410` | 46 | UnwindData |  |
| 397 | `SHCoCreateInstanceWorker` | `0x6F450` | 136 | UnwindData |  |
| 348 | `PathIsEqualOrSubFolderOfKnownFolders` | `0x74320` | 299 | UnwindData |  |
| 445 | `SHGetCorrectOwnerSid` | `0x744F0` | 1,602 | UnwindData |  |
| 347 | `PathIsEqualOrSubFolder` | `0x75020` | 336 | UnwindData |  |
| 415 | `SHCreateItemFromParsingName` | `0x76620` | 1,098 | UnwindData |  |
| 373 | `RebaseOnDriveLetter` | `0x794B0` | 558 | UnwindData |  |
| 923 | *Ordinal Only* | `0x7B180` | 302 | UnwindData |  |
| 2003 | *Ordinal Only* | `0x7C250` | 29,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `AssocGetDetailsOfPropKey` | `0x83620` | 359 | UnwindData |  |
| 490 | `SHGetUIObjectOfItem` | `0x83F20` | 174 | UnwindData |  |
| 461 | `SHGetImageList` | `0x85930` | 189 | UnwindData |  |
| 79 | `_IsSHILInited` | `0x85D90` | 52 | UnwindData |  |
| 237 | `GetThreadFlags` | `0x8C470` | 95 | UnwindData |  |
| 444 | `SHGetComputerDisplayName` | `0x8EA90` | 557 | UnwindData |  |
| 26 | `GetShellIconLocationParts` | `0x91340` | 227 | UnwindData |  |
| 487 | `SHGetStockIconInfo` | `0x91430` | 317 | UnwindData |  |
| 24 | `GetShellIconLocation` | `0x91770` | 374 | UnwindData |  |
| 376 | `RegGetValueString` | `0x92AC0` | 200 | UnwindData |  |
| 914 | *Ordinal Only* | `0x95660` | 315 | UnwindData |  |
| 161 | `CreateSortColumnArray` | `0x95FB0` | 194 | UnwindData |  |
| 212 | `GetCachedIniForFolder` | `0x965C0` | 228 | UnwindData |  |
| 645 | `SHChangeNotification_Unlock` | `0x966B0` | 5,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `CFreeThreadedItemContainer_CreateInstance` | `0x97AE0` | 273 | UnwindData |  |
| 280 | `ILCloneFirst` | `0x99E60` | 228 | UnwindData |  |
| 414 | `SHCreateItemFromIDList` | `0x9B500` | 784 | UnwindData |  |
| 418 | `SHCreateItemWithParent` | `0x9B820` | 801 | UnwindData |  |
| 136 | `CShellItem_CreateInstance` | `0x9BC50` | 78 | UnwindData |  |
| 389 | `SHBindToObject` | `0xA67E0` | 2,926 | UnwindData |  |
| 100 | `SHRestricted` | `0xA7990` | 58 | UnwindData |  |
| 109 | `CFSFolder_CreateFolder` | `0xA8430` | 202 | UnwindData |  |
| 602 | `ShowSuperHidden` | `0xAA510` | 163 | UnwindData |  |
| 68 | `SHGetSetSettings` | `0xAB0B0` | 446 | UnwindData |  |
| 403 | `SHCreateDefaultExtractIcon` | `0xAD420` | 198 | UnwindData |  |
| 468 | `SHGetKnownFolderPath` | `0xB11D0` | 4,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `IsDelegateRegId` | `0xB2330` | 6,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 494 | `SHILAliasTranslate` | `0xB3BB0` | 1,958 | UnwindData |  |
| 286 | `ILFindLastID` | `0xB7B60` | 10,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 911 | *Ordinal Only* | `0xBA510` | 639 | UnwindData |  |
| 358 | `PathIsSystemDrive` | `0xBAA90` | 131 | UnwindData |  |
| 71 | `TopViewDescription_GetGroupByProperty` | `0xBC230` | 107 | UnwindData |  |
| 851 | *Ordinal Only* | `0xBCD30` | 159 | UnwindData |  |
| 823 | *Ordinal Only* | `0xBCDE0` | 29 | UnwindData |  |
| 789 | *Ordinal Only* | `0xBD310` | 163 | UnwindData |  |
| 791 | *Ordinal Only* | `0xBD400` | 61 | UnwindData |  |
| 788 | *Ordinal Only* | `0xBE550` | 591 | UnwindData |  |
| 275 | `HideExtension` | `0xD6B40` | 300 | UnwindData |  |
| 916 | *Ordinal Only* | `0xE0E20` | 291 | UnwindData |  |
| 915 | *Ordinal Only* | `0xE1610` | 800 | UnwindData |  |
| 385 | `SHAssocEnumHandlers` | `0xE1BB0` | 133 | UnwindData |  |
| 322 | `IsProgramAccessEnabled` | `0xE1DA0` | 400 | UnwindData |  |
| 399 | `SHCreateAssocHandler` | `0xE1F40` | 68 | UnwindData |  |
| 318 | `IsNullTime` | `0xE4030` | 75 | UnwindData |  |
| 351 | `PathIsLnk` | `0xE6D40` | 65 | UnwindData |  |
| 346 | `PathIsBinaryExe` | `0xE6D90` | 113 | UnwindData |  |
| 850 | *Ordinal Only* | `0xE9680` | 43 | UnwindData |  |
| 430 | `SHDefExtractIconW` | `0xF5A60` | 834 | UnwindData |  |
| 88 | `AssocCreateStateRepoElement` | `0xF6230` | 989 | UnwindData |  |
| 308 | `IsElevationRequired` | `0xF8B70` | 295 | UnwindData |  |
| 349 | `PathIsExe` | `0xF8EB0` | 113 | UnwindData |  |
| 146 | `CheckSmartScreenWithAltFile` | `0xF9170` | 526 | UnwindData |  |
| 478 | `SHGetPathFromIDListAlloc` | `0xFEDC0` | 899 | UnwindData |  |
| 394 | `SHChangeNotify` | `0xFF150` | 1,065 | UnwindData |  |
| 27 | `ILSaveToStream` | `0x100110` | 177 | UnwindData |  |
| 946 | `SHChangeNotifySuspendResume` | `0x100C70` | 174 | UnwindData |  |
| 330 | `MapIDListToIconILIndex` | `0x10C710` | 179 | UnwindData |  |
| 873 | *Ordinal Only* | `0x10D5A0` | 140 | UnwindData |  |
| 70 | `Shell_GetStockImageIndex` | `0x10DE50` | 622 | UnwindData |  |
| 54 | `PathContainedByManifestedKnownFolder_FullTrustCaller_ForPackage` | `0x114070` | 1,546 | UnwindData |  |
| 2002 | *Ordinal Only* | `0x115410` | 315 | UnwindData |  |
| 75 | `PathYetAnotherMakeUniqueName` | `0x11CFB0` | 336 | UnwindData |  |
| 342 | `PathFileExistsForUniqueName` | `0x11D8D0` | 371 | UnwindData |  |
| 230 | `GetStartIndexFromUniqueNameTemplate` | `0x11DE00` | 178 | UnwindData |  |
| 401 | `SHCreateDataObject` | `0x11E7F0` | 139 | UnwindData |  |
| 264 | *Ordinal Only* | `0x11F3C0` | 302 | UnwindData |  |
| 740 | *Ordinal Only* | `0x11F760` | 125 | UnwindData |  |
| 217 | `GetFindDataForPath` | `0x1258C0` | 1,626 | UnwindData |  |
| 163 | `CreateVolatilePropertyStore` | `0x13A4A0` | 196 | UnwindData |  |
| 943 | `CreateExtrinsicPropertyStore` | `0x13B090` | 226 | UnwindData |  |
| 764 | *Ordinal Only* | `0x13CBE0` | 1,984 | UnwindData |  |
| 158 | `CreateLinkFromItem` | `0x1520D0` | 371 | UnwindData |  |
| 581 | `SetLinkFlags` | `0x152810` | 173 | UnwindData |  |
| 416 | `SHCreateItemFromRelativeName` | `0x153D90` | 313 | UnwindData |  |
| 847 | *Ordinal Only* | `0x155C30` | 296 | UnwindData |  |
| 819 | *Ordinal Only* | `0x159BB0` | 250 | UnwindData |  |
| 464 | `SHGetItemFromObject` | `0x15E540` | 152 | UnwindData |  |
| 291 | `ILGetSize` | `0x1607E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `DllGetClassObject` | `0x160810` | 746 | UnwindData |  |
| 375 | `RegGetFirstShotQISearch` | `0x160C60` | 273 | UnwindData |  |
| 371 | `QueryStorageAccess_FullTrustCaller_ForToken` | `0x162D60` | 310 | UnwindData |  |
| 11 | `CreateStorageItemFromPath_FullTrustCaller_ForPackage` | `0x163170` | 173 | UnwindData |  |
| 925 | `CreateStorageItemFromShellItem_FullTrustCaller_ForPackage` | `0x163230` | 55 | UnwindData |  |
| 546 | `STORAGE_CreateStorageItemFromShellItem_FullTrustCaller_ForPackage` | `0x163230` | 55 | UnwindData |  |
| 281 | `ILCombine` | `0x16B820` | 32 | UnwindData |  |
| 432 | `SHEvaluateSystemCommandTemplate` | `0x16BF10` | 28 | UnwindData |  |
| 84 | `App_IsLFNAware` | `0x16CA00` | 440 | UnwindData |  |
| 396 | `SHCloneSpecialIDList` | `0x177910` | 72 | UnwindData |  |
| 484 | `SHGetSpecialFolderLocation` | `0x177B80` | 37 | UnwindData |  |
| 454 | `SHGetFolderLocation` | `0x177BB0` | 395 | UnwindData |  |
| 497 | `SHKnownFolderFromCSIDL` | `0x177D50` | 3,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `CCachedShellItem_CreateInstance` | `0x1789B0` | 237 | UnwindData |  |
| 374 | `RebaseOnVolumeID` | `0x183EF0` | 600 | UnwindData |  |
| 144 | `CheckElevatedPermissionToShellItem` | `0x1846D0` | 713 | UnwindData |  |
| 157 | `CreateItemFromLink` | `0x188050` | 133 | UnwindData |  |
| 156 | `CreateItemArrayFromObjectArray` | `0x18D430` | 146 | UnwindData |  |
| 295 | `ILRemoveLastID` | `0x193F20` | 82,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `StateRepoVerbsCache_GetContextMenuVerbs` | `0x1A7FB0` | 134 | UnwindData |  |
| 271 | `GoModal` | `0x1AD650` | 46 | UnwindData |  |
| 32 | `GetThumbnailCutoffFromType` | `0x1AF320` | 231 | UnwindData |  |
| 180 | `DllMain` | `0x1B2030` | 414 | UnwindData |  |
| 196 | `EnumShellItemsFromUnknown` | `0x1B8BD0` | 489 | UnwindData |  |
| 425 | `SHCreateShellItemArrayFromIDLists` | `0x1B9020` | 149 | UnwindData |  |
| 846 | `ILLoadFromStreamEx` | `0x1C9AE0` | 305 | UnwindData |  |
| 219 | `GetFolderString` | `0x1C9E60` | 225 | UnwindData |  |
| 367 | `PathResolve` | `0x1CE6F0` | 562 | UnwindData |  |
| 285 | `ILFindChild` | `0x1D8230` | 524 | UnwindData |  |
| 164 | `CustomStatePropertyDescription_CreateWithItemPropertyStore` | `0x1DA9F0` | 194 | UnwindData |  |
| 482 | `SHGetSetFolderCustomSettings` | `0x1DC8D0` | 414 | UnwindData |  |
| 52 | `IsUnderKnownFolder` | `0x1E0490` | 374 | UnwindData |  |
| 307 | `IsDesktopExplorerProcess` | `0x1E3D50` | 39,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 621 | `Win32RemoveDirectory` | `0x1ED740` | 202 | UnwindData |  |
| 781 | *Ordinal Only* | `0x1EFD60` | 172 | UnwindData |  |
| 315 | `IsLibraryPolicyEnabled` | `0x1F2800` | 110 | UnwindData |  |
| 232 | `GetSystemPersistedStorageItemList` | `0x1F96A0` | 308 | UnwindData |  |
| 123 | `CItemStore_CreateInstance` | `0x1FBB70` | 182 | UnwindData |  |
| 498 | `SHKnownFolderToCSIDL` | `0x1FC260` | 38 | UnwindData |  |
| 412 | `SHCreateFileExtractIconW` | `0x1FC630` | 263 | UnwindData |  |
| 159 | `CreateLinkToPidl` | `0x1FC9A0` | 1,288 | UnwindData |  |
| 339 | `PathCleanupSpec` | `0x1FD500` | 350 | UnwindData |  |
| 453 | `SHGetFileInfoW` | `0x1FD670` | 654 | UnwindData |  |
| 121 | `CItemSetOperations_CreateInstance` | `0x2027B0` | 135 | UnwindData |  |
| 218 | `GetFindDataFromFileInformationByHandle` | `0x205DA0` | 380 | UnwindData |  |
| 387 | `SHBindToFolderIDListParent` | `0x206AF0` | 250 | UnwindData |  |
| 287 | `ILFree` | `0x209990` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 440 | `SHFree` | `0x209990` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `CRegFolder_CreateAndInit` | `0x209B70` | 233 | UnwindData |  |
| 345 | `PathGetShortPath` | `0x20CF70` | 160 | UnwindData |  |
| 110 | `CFSFolder_IsCommonItem` | `0x20E370` | 14,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 594 | `Shell_GetCachedImageIndexW` | `0x211C90` | 239 | UnwindData |  |
| 611 | `Stream_ReadStringCoAllocW` | `0x212B50` | 308 | UnwindData |  |
| 613 | `Stream_WriteStringW` | `0x216010` | 154 | UnwindData |  |
| 395 | `SHChangeNotifyRegisterThread` | `0x217AE0` | 69 | UnwindData |  |
| 321 | `IsProcessAnExplorer` | `0x2197A0` | 140 | UnwindData |  |
| 361 | `PathIsWild` | `0x21AC40` | 57 | UnwindData |  |
| 283 | `ILCreateFromPathEx` | `0x21B970` | 168 | UnwindData |  |
| 151 | `CountFiles` | `0x21BB60` | 86 | UnwindData |  |
| 437 | `SHFileOperationWithAdditionalFlags` | `0x21BC30` | 524 | UnwindData |  |
| 245 | `SHTestTokenMembership` | `0x21D170` | 225 | UnwindData |  |
| 147 | `SHCLSIDFromString` | `0x2203C0` | 53 | UnwindData |  |
| 419 | `SHCreateItemWithParentAndChildId` | `0x221290` | 168 | UnwindData |  |
| 352 | `PathIsOneOf` | `0x225CA0` | 378 | UnwindData |  |
| 33 | `GetUserChoiceForUrl` | `0x235960` | 952 | UnwindData |  |
| 143 | `CViewSettings_CreateInstance` | `0x23A450` | 150 | UnwindData |  |
| 86 | `AssocCreateForClasses` | `0x23B370` | 313 | UnwindData |  |
| 577 | `SetAppStartingCursor` | `0x2416F0` | 191 | UnwindData |  |
| 130 | `CRegFolder_CreateInstance` | `0x241970` | 200 | UnwindData |  |
| 114 | `CFolderExtractImage_Create` | `0x243810` | 249 | UnwindData |  |
| 170 | `DataAccessCaches_InvalidateForLibrary` | `0x245100` | 63 | UnwindData |  |
| 103 | `CCategoryProvider_CreateWithParams` | `0x245A40` | 277 | UnwindData |  |
| 426 | `SHCreateShellItemArrayFromShellItem` | `0x247440` | 277 | UnwindData |  |
| 250 | `Global_WindowsStorage_csIconCache` | `0x248EC0` | 17,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 644 | `SHChangeNotification_Lock` | `0x24D410` | 128 | UnwindData |  |
| 489 | `SHGetUIObjectOf` | `0x24E060` | 161 | UnwindData |  |
| 405 | `SHCreateDelegatingTransfer` | `0x24EF60` | 164 | UnwindData |  |
| 2000 | *Ordinal Only* | `0x252960` | 918 | UnwindData |  |
| 521 | `SHSetTemporaryPropertyForItem` | `0x2533E0` | 193 | UnwindData |  |
| 377 | `RegistryVerbs_GetHandlerMultiSelectModel` | `0x2553A0` | 207 | UnwindData |  |
| 255 | `Global_WindowsStorage_fEndInitialized` | `0x259900` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | *Ordinal Only* | `0x259BC0` | 153 | UnwindData |  |
| 765 | *Ordinal Only* | `0x25B3C0` | 230 | UnwindData |  |
| 830 | *Ordinal Only* | `0x25B8D0` | 162 | UnwindData |  |
| 627 | `_PredictReasonableImpact` | `0x25C1E0` | 194 | UnwindData |  |
| 306 | `IsDesktopBandWindow` | `0x25D720` | 82 | UnwindData |  |
| 296 | `ILStreamSize` | `0x261AC0` | 23,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 824 | *Ordinal Only* | `0x267720` | 322 | UnwindData |  |
| 167 | `DAD_DragEnterEx` | `0x268FA0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `DAD_SetDragImage` | `0x268FA0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `DAD_ShowDragImage` | `0x268FA0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `IsLFNDriveA` | `0x268FA0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `IsLFNDriveW` | `0x268FA0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `SHShouldShowWizards` | `0x268FA0` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `FilterOnAttributes` | `0x269550` | 14,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 457 | `SHGetFolderPathAndSubDirW` | `0x26CE50` | 270 | UnwindData |  |
| 290 | `ILGetNext` | `0x26CF70` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | *Ordinal Only* | `0x26D0F0` | 118 | UnwindData |  |
| 247 | `Global_WindowsStorage_Untyped_rgshil` | `0x26D470` | 6,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 568 | `STORAGE_SHGetDesktopFolderWorker` | `0x26ECF0` | 6,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 495 | `SHIsCurrentThreadOnUserDesktop` | `0x2704E0` | 505 | UnwindData |  |
| 2001 | *Ordinal Only* | `0x2711A0` | 164 | UnwindData |  |
| 185 | `DoesBoundedItemArrayMatchAQS` | `0x272940` | 431 | UnwindData |  |
| 413 | `SHCreateFilterFromFullText` | `0x272C50` | 563 | UnwindData |  |
| 815 | *Ordinal Only* | `0x273670` | 51 | UnwindData |  |
| 609 | `StorageItemHelpers_IsSupportedRemovablePath` | `0x276050` | 40 | UnwindData |  |
| 257 | `Global_WindowsStorage_fIconCacheIsValid` | `0x277AB0` | 5,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 817 | *Ordinal Only* | `0x278E40` | 267 | UnwindData |  |
| 317 | `IsNonEnumPolicySet` | `0x27BD10` | 185 | UnwindData |  |
| 254 | `Global_WindowsStorage_esServerMode` | `0x27C1F0` | 9,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `Global_WindowsStorage_Untyped_MountPoint` | `0x27E700` | 2,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `SHGetSpecialFolderPathA` | `0x27F240` | 55 | UnwindData |  |
| 455 | `SHGetFolderPathA` | `0x27F280` | 146 | UnwindData |  |
| 223 | `GetRegDataDrivenCommand` | `0x2819C0` | 38 | UnwindData |  |
| 224 | `GetRegDataDrivenCommandWithAssociation` | `0x2819F0` | 301 | UnwindData |  |
| 428 | `SHCreateStdEnumFmtEtcEx` | `0x281C60` | 699 | UnwindData |  |
| 74 | `SHCreateStdEnumFmtEtc` | `0x281F30` | 213 | UnwindData |  |
| 135 | `CShellItemArray_CreateInstance` | `0x285490` | 123 | UnwindData |  |
| 216 | `GetFileUndoText` | `0x28E930` | 224 | UnwindData |  |
| 849 | *Ordinal Only* | `0x294EA0` | 43 | UnwindData |  |
| 248 | `Global_WindowsStorage_afNotRedirected` | `0x296FD0` | 7,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 913 | *Ordinal Only* | `0x298EE0` | 320 | UnwindData |  |
| 604 | `SplitFileNameAndExtension` | `0x299030` | 189 | UnwindData |  |
| 53 | `LoadNameTemplate` | `0x299100` | 289 | UnwindData |  |
| 249 | `Global_WindowsStorage_ccIcon` | `0x29E370` | 15,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | *Ordinal Only* | `0x2A1EA0` | 77 | UnwindData |  |
| 220 | `GetFolderType` | `0x2A2E80` | 1,869 | UnwindData |  |
| 85 | `ArrangeWindows` | `0x2A76D0` | 23,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `DAD_AutoScroll` | `0x2A76D0` | 23,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `DllRegisterServer` | `0x2A76D0` | 23,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `DllUnregisterServer` | `0x2A76D0` | 23,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `InternalExtractIconListA` | `0x2A76D0` | 23,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `InternalExtractIconListW` | `0x2A76D0` | 23,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `IsValidIDList` | `0x2A76D0` | 23,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `IsValidIDListObject` | `0x2A76D0` | 23,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 380 | `SFVCB_OnAddPropertyPages` | `0x2A76D0` | 23,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `CTaskAddDoc_Create` | `0x2AD3E0` | 229 | UnwindData |  |
| 268 | `Global_WindowsStorage_tlsIconCache` | `0x2ADBC0` | 3,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2009 | *Ordinal Only* | `0x2AEA50` | 24,395 | UnwindData |  |
| 265 | `Global_WindowsStorage_lrFlags` | `0x2B83B0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `GetVolumeMountPath` | `0x2B8520` | 331 | UnwindData |  |
| 492 | `SHGetUserDisplayName` | `0x2BA3F0` | 444 | UnwindData |  |
| 240 | `Global_WindowsStorage_Untyped_FileClassSRWLock` | `0x2BAEA0` | 1,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 614 | `TBCRegisterObjectParam` | `0x2BB350` | 268 | UnwindData |  |
| 344 | `PathGetPathDisplayName` | `0x2BED40` | 108 | UnwindData |  |
| 825 | *Ordinal Only* | `0x2BEF20` | 204 | UnwindData |  |
| 80 | `_ustrcmp` | `0x2C35A0` | 57 | UnwindData |  |
| 383 | `SHAddIconsToCache` | `0x2C70B0` | 229 | UnwindData |  |
| 176 | `DetermineFolderDestinationParentAppID` | `0x2C8EB0` | 648 | UnwindData |  |
| 480 | `SHGetPathFromIDListW` | `0x2CAF40` | 162 | UnwindData |  |
| 2005 | *Ordinal Only* | `0x2CC1E0` | 71 | UnwindData |  |
| 55 | `QueryNewMaxIcons` | `0x2CEC10` | 144 | UnwindData |  |
| 242 | `Global_WindowsStorage_Untyped_pFileClassCacheTable` | `0x2D0340` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `GetShellClassInfoInfoTip` | `0x2D0870` | 90 | UnwindData |  |
| 227 | `GetShellClassInfo` | `0x2D0980` | 159 | UnwindData |  |
| 226 | `GetSelectionStateFromItemArray` | `0x2D4410` | 168 | UnwindData |  |
| 252 | `Global_WindowsStorage_dwThreadBindCtx` | `0x2D95E0` | 6,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `PathIsTemporaryW` | `0x2DADD0` | 66 | UnwindData |  |
| 253 | `Global_WindowsStorage_dwThreadInitializing` | `0x2DB9D0` | 4,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `StateRepoVerbsCache_Destroy` | `0x2DC970` | 37 | UnwindData |  |
| 104 | `CCollectionFactory_CreateInstance` | `0x2DEB10` | 288 | UnwindData |  |
| 120 | `CItemHandlerCache_CreateInstance` | `0x2DF670` | 173 | UnwindData |  |
| 2007 | *Ordinal Only* | `0x2E39D0` | 21,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `GetFileSizeOnDisk` | `0x2E8CC0` | 92 | UnwindData |  |
| 6 | `AssocKeyFromElement` | `0x2E8ED0` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 493 | `SHHandleUpdateImage` | `0x2E9600` | 137 | UnwindData |  |
| 313 | `IsLUAEnabled` | `0x2E98C0` | 75 | UnwindData |  |
| 562 | `STORAGE_SHCreateShellItemArrayFromDataObject` | `0x2EDCF0` | 1,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 818 | *Ordinal Only* | `0x2EE450` | 4,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 555 | `STORAGE_SHAddToRecentDocs` | `0x2EF500` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `STORAGE_SHCreateShellItemArrayFromIDLists` | `0x2EF5F0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2006 | *Ordinal Only* | `0x2EF860` | 2,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `Global_WindowsStorage_MaxIcons` | `0x2F0200` | 3,552 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 561 | `STORAGE_SHCreateShellItemArray` | `0x2F0FE0` | 2,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 582 | `SetThreadFlags` | `0x2F1B60` | 153 | UnwindData |  |
| 108 | `CFSFolder_AdjustForSlowColumn` | `0x2F22B0` | 2,256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 564 | `STORAGE_SHCreateShellItemArrayFromShellItem` | `0x2F2B80` | 2,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 381 | `SHAddDefaultProperties` | `0x2F3470` | 352 | UnwindData |  |
| 139 | `CStorageItem_GetValidatedStorageItemObject` | `0x2F4190` | 156 | UnwindData |  |
| 64 | `SHGetCategorizer` | `0x2F7540` | 427 | UnwindData |  |
| 417 | `SHCreateItemInKnownFolder` | `0x2F7C80` | 241 | UnwindData |  |
| 263 | `Global_WindowsStorage_lProcessClassCount` | `0x2FAF20` | 4,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `CFSTransfer_CreateInstance` | `0x2FBEF0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 481 | `SHGetRealIDL` | `0x2FBF80` | 3,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `CreateStorageItemFromShellItem` | `0x2FCC80` | 8,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 534 | `STORAGE_AddItemToRecentDocs` | `0x2FEF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `CPrivateProfileCache_Save` | `0x2FEF80` | 77 | UnwindData |  |
| 260 | `Global_WindowsStorage_iLastSysIcon` | `0x2FEFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 565 | `STORAGE_SHFileOperation` | `0x2FF000` | 4,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `AssocShouldProcessUseAppToAppLaunching` | `0x2FFFB0` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 680 | `IsUserAnAdmin` | `0x3004E0` | 6,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 261 | `Global_WindowsStorage_iLastSystemColorDepth` | `0x301F00` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 258 | `Global_WindowsStorage_fNeedsInitBroadcast` | `0x302190` | 5,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `STORAGE_CreateStorageItemFromShellItem_FullTrustCaller_ForPackage_WithProcessHandleAndSecondaryStreamName` | `0x3037A0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `STORAGE_FillResultWithNullForKeys` | `0x3037A0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 897 | *Ordinal Only* | `0x3037A0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 503 | `SHMapIDListToSystemImageListIndexAsync2` | `0x303AD0` | 456 | UnwindData |  |
| 538 | `STORAGE_CStorageItem_GetValidatedStorageItem` | `0x305140` | 6,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `CreateStorageItemFromPath_PartialTrustCaller` | `0x306960` | 174 | UnwindData |  |
| 551 | `STORAGE_GetShellItemFromStorageItem` | `0x307C40` | 3,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `ICIX2SEI` | `0x308B90` | 285 | UnwindData |  |
| 450 | `SHGetDiskFreeSpaceExW` | `0x30AF20` | 12,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `ICI2ICIX` | `0x30DE80` | 513 | UnwindData |  |
| 256 | `Global_WindowsStorage_fIconCacheHasBeenSuccessfullyCreated` | `0x30F6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `Global_WindowsStorage_Untyped_pFileHanderMap` | `0x30F6E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `CShellItemArrayAsVirtualizedObjectArray_CreateInstance` | `0x30F6F0` | 123 | UnwindData |  |
| 409 | `SHCreateDirectoryExW` | `0x30FE30` | 9,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `SHCreateDirectoryExWStub` | `0x30FE30` | 9,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 560 | `STORAGE_SHCreateDirectoryExWWorker` | `0x30FE30` | 9,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `OpenRegStream` | `0x312490` | 2,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `DestroyHashItemTable` | `0x312CC0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `DllCanUnloadNow` | `0x312F40` | 93 | UnwindData |  |
| 49 | `IsRemovableDevicePath` | `0x3298F0` | 187 | UnwindData |  |
| 600 | `ShouldUseStorageProviderViews` | `0x32AD60` | 277 | UnwindData |  |
| 178 | `DllGetActivationFactory` | `0x32C520` | 77 | UnwindData |  |
| 433 | `SHExtCoCreateInstanceString` | `0x32C720` | 139 | UnwindData |  |
| 210 | `FreeIconList` | `0x341F00` | 12,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `InvalidateDriveType` | `0x341F00` | 12,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `PathIsShortcutToProgram` | `0x345090` | 507 | UnwindData |  |
| 354 | `PathIsShortcut` | `0x3452A0` | 92 | UnwindData |  |
| 502 | `SHMapIDListToSystemImageListIndexAsync` | `0x34D630` | 86 | UnwindData |  |
| 93 | `BrokerAppSiloShellItemsForApplicationUserModelId` | `0x34E080` | 132 | UnwindData |  |
| 94 | `BrokerAppSiloShellItemsForPackageFamilyName` | `0x34E110` | 1,145 | UnwindData |  |
| 316 | `IsNameListedUnderKey` | `0x351670` | 361 | UnwindData |  |
| 443 | `SHGetCompressedFileSizeW` | `0x351A70` | 240 | UnwindData |  |
| 112 | `CFileOperationRecorder_CreateInstance` | `0x3521A0` | 163 | UnwindData |  |
| 549 | `STORAGE_CreateStorageItemFromShellItem_FullTrustCaller_UseImplicitFlagsAndPackage` | `0x3557B0` | 6,784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | *Ordinal Only* | `0x357230` | 33 | UnwindData |  |
| 10 | `CreateStorageItemFromPath_FullTrustCaller` | `0x3583A0` | 26 | UnwindData |  |
| 542 | `STORAGE_CreateStorageItemFromPath_FullTrustCaller` | `0x3583A0` | 26 | UnwindData |  |
| 406 | `SHCreateDirectory` | `0x35AC50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `SHCreateDirectoryStub` | `0x35AC50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 558 | `STORAGE_SHCreateDirectory` | `0x35AC50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 620 | `Win32DeleteFile` | `0x35AC90` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 386 | `SHAssocEnumHandlersForProtocolByApplication` | `0x35AD20` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `Global_WindowsStorage_hwndSCN` | `0x35AFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `Global_WindowsStorage_nImageManagerVersion` | `0x35B000` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `Global_WindowsStorage_csSCN` | `0x35B060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `Global_WindowsStorage_ulNextID` | `0x35B080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `Global_WindowsStorage_tlsThreadFlags` | `0x35B090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `Global_WindowsStorage_iUseLinkPrefix` | `0x35B0A0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `Global_WindowsStorage_tlsChangeClientProxy` | `0x35B0F0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `SHGetUserNameW` | `0x35B1B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | *Ordinal Only* | `0x35B1E0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2004 | *Ordinal Only* | `0x35B440` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | *Ordinal Only* | `0x35B4F0` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `Window_IsLFNAware` | `0x35BA80` | 37 | UnwindData |  |
| 598 | `ShortSizeFormat64` | `0x35BC70` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 407 | `SHCreateDirectoryExA` | `0x35BD00` | 57,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 408 | `SHCreateDirectoryExAStub` | `0x35BD00` | 57,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 559 | `STORAGE_SHCreateDirectoryExA` | `0x35BD00` | 57,408 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | *Ordinal Only* | `0x369D40` | 863 | UnwindData |  |
| 816 | *Ordinal Only* | `0x36A0B0` | 160 | UnwindData |  |
| 844 | *Ordinal Only* | `0x36A160` | 156 | UnwindData |  |
| 87 | `AssocCreateListForClasses` | `0x3A9AC0` | 207,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `GetCachedFileUpdateInformation` | `0x3DC470` | 18 | UnwindData |  |
| 945 | `GetInfoForFileInUse` | `0x3E09F0` | 89 | UnwindData |  |
| 233 | `GetSystemPersistedStorageItemListForUser` | `0x3E0BC0` | 345 | UnwindData |  |
| 272 | `GrantPathAccess_FullTrustCaller_ForPackage` | `0x3E0D20` | 187 | UnwindData |  |
| 273 | `GrantWorkingDirectoryAccess_FullTrustCaller_ForPackage` | `0x3E0DF0` | 193 | UnwindData |  |
| 370 | `QueryStorageAccess_FullTrustCaller_ForPackage` | `0x3E0EC0` | 503 | UnwindData |  |
| 610 | `Storage_Internal_GetAccessListForPackage` | `0x3E10C0` | 315 | UnwindData |  |
| 462 | `SHGetInstanceExplorer` | `0x3E12A0` | 814,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ApplyProviderSettings` | `0x4A8090` | 201 | UnwindData |  |
| 14 | `GatherProviderSettings` | `0x4A8750` | 230 | UnwindData |  |
| 60 | `RegisterChangeNotifications` | `0x4A89F0` | 944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `UnregisterChangeNotifications` | `0x4A8DA0` | 9,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `CreateLocalizationDesktopIni` | `0x4AB2B0` | 89 | UnwindData |  |
| 508 | `SHPrepareKnownFoldersCommon` | `0x4AB310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 509 | `SHPrepareKnownFoldersUser` | `0x4AB320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 519 | `SHSetKnownFolderPath` | `0x4AB330` | 28,176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2008 | *Ordinal Only* | `0x4B2140` | 52 | UnwindData |  |
| 150 | `CopyDefaultLibrariesFromGroupPolicy` | `0x4B5E90` | 250 | UnwindData |  |
| 314 | `IsLibraryCreatedByPolicy` | `0x4B5F90` | 388 | UnwindData |  |
| 514 | `SHResolveLibrary` | `0x4B9A40` | 62 | UnwindData |  |
| 155 | `CreateItemArrayFromItemStore` | `0x4C68D0` | 167 | UnwindData |  |
| 195 | `EnumShellItemsFromEnumFullIdList` | `0x4C6980` | 175 | UnwindData |  |
| 427 | `SHCreateShellItemArrayWithFolderParent` | `0x4C6AD0` | 165 | UnwindData |  |
| 124 | `CMruLongList_CreateInstance` | `0x508720` | 231 | UnwindData |  |
| 626 | `_CleanRecentDocs` | `0x510BF0` | 679 | UnwindData |  |
| 948 | `CreateFileMetadataCache` | `0x51B680` | 65 | UnwindData |  |
| 947 | `CreateStorageProviderPropertyStore` | `0x51E250` | 284 | UnwindData |  |
| 165 | `CustomStatePropertyDescription_CreateWithStateIdentifier` | `0x51E6E0` | 171 | UnwindData |  |
| 213 | `GetCommandProviderForFolderType` | `0x52D450` | 124 | UnwindData |  |
| 456 | `SHGetFolderPathAndSubDirA` | `0x531080` | 214 | UnwindData |  |
| 517 | `SHSetFolderPathA` | `0x531160` | 121 | UnwindData |  |
| 518 | `SHSetFolderPathW` | `0x5311E0` | 253 | UnwindData |  |
| 535 | `STORAGE_AddNewFolderToFrequentPlaces` | `0x5312F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 536 | `STORAGE_CEnumFiles_CreateInstance` | `0x531300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 537 | `STORAGE_CStatusProvider_CreateInstance` | `0x531310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 539 | `STORAGE_CStorageItem_GetValidatedStorageItemObject` | `0x531320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 540 | `STORAGE_ClearDestinationsForAllApps` | `0x531330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `STORAGE_CreateSortColumnArrayFromListDesc` | `0x531340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 543 | `STORAGE_CreateStorageItemFromPath_FullTrustCaller_ForPackage` | `0x531350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 544 | `STORAGE_CreateStorageItemFromPath_PartialTrustCaller` | `0x531360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 545 | `STORAGE_CreateStorageItemFromShellItem_FullTrustCaller` | `0x531370` | 26 | UnwindData |  |
| 547 | `STORAGE_CreateStorageItemFromShellItem_FullTrustCaller_ForPackage_WithProcessHandle` | `0x531390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 552 | `STORAGE_GetSystemPersistedStorageItemList` | `0x5313A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `STORAGE_MakeDestinationItem` | `0x5313B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 554 | `STORAGE_PathIsEqualOrSubFolderOfKnownFolders` | `0x5313C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 556 | `STORAGE_SHAddToRecentDocsEx` | `0x5313D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `STORAGE_SHConfirmOperation` | `0x5313E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 566 | `STORAGE_SHFileOperationA` | `0x5313F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 567 | `STORAGE_SHFreeNameMappings` | `0x531400` | 98 | UnwindData |  |
| 569 | `STORAGE_SHGetPathFromMsUri` | `0x531470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 570 | `STORAGE_SHOpenFolderAndSelectItems` | `0x531480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 571 | `STORAGE_SHPathPrepareForWriteA` | `0x531490` | 114 | UnwindData |  |
| 572 | `STORAGE_SHPathPrepareForWriteW` | `0x531510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 573 | `STORAGE_SHValidateMSUri` | `0x531520` | 41,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `StateRepoVerbsCache_RebuildCacheAsync` | `0x53B8D0` | 122 | UnwindData |  |
| 1003 | *Ordinal Only* | `0x5914A0` | 163 | UnwindData |  |
| 761 | *Ordinal Only* | `0x591550` | 123 | UnwindData |  |
| 530 | `SHUpdateImageA` | `0x5915E0` | 106 | UnwindData |  |
| 531 | `SHUpdateImageW` | `0x591650` | 240 | UnwindData |  |
| 3 | `AllowRecycleBinOnVolume` | `0x591810` | 319 | UnwindData |  |
| 13 | `EnsureRecycleBinLocation` | `0x5919F0` | 168 | UnwindData |  |
| 16 | `GetDefaultMaxCapacity` | `0x591AA0` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetRecreatableRecycleBinLocation` | `0x591D20` | 389 | UnwindData |  |
| 21 | `GetRecycleBinKey` | `0x591EB0` | 218 | UnwindData |  |
| 22 | `GetRecycleBinLocation` | `0x591F90` | 211 | UnwindData |  |
| 23 | `GetRecycleBinPath` | `0x592070` | 178 | UnwindData |  |
| 34 | `GetVolumeGUIDFromVolumeName` | `0x5921D0` | 58 | UnwindData |  |
| 47 | `IsRecycleBinIconEmpty` | `0x5922C0` | 348 | UnwindData |  |
| 48 | `IsRecycleBinKnownFolder` | `0x592430` | 556 | UnwindData |  |
| 67 | `SHUpdateRecycleBinIconEx` | `0x592D80` | 70 | UnwindData |  |
| 510 | `SHQueryRecycleBinA` | `0x5939D0` | 149 | UnwindData |  |
| 511 | `SHQueryRecycleBinW` | `0x593A70` | 323 | UnwindData |  |
| 532 | `SHUpdateRecycleBinIcon` | `0x593BC0` | 57 | UnwindData |  |
| 617 | `UpdateRecycleBinIcon` | `0x593C00` | 1,563 | UnwindData |  |
| 7 | `BuildName` | `0x594230` | 736 | UnwindData |  |
| 12 | `DrawTransparentBackground` | `0x594F70` | 334 | UnwindData |  |
| 18 | `GetMonitorRects` | `0x595310` | 221 | UnwindData |  |
| 19 | `GetPrimaryMonitor` | `0x5954A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `GetStringsFromFormat` | `0x5954D0` | 236 | UnwindData |  |
| 36 | `HrLoadString` | `0x5956B0` | 37 | UnwindData |  |
| 38 | `ImageList_GetMirrored` | `0x5956E0` | 127 | UnwindData |  |
| 39 | `ImageList_MirroredDraw` | `0x595770` | 164 | UnwindData |  |
| 40 | `InitDeletedItem` | `0x595820` | 115 | UnwindData |  |
| 43 | `IsFolderPicker` | `0x595B50` | 144 | UnwindData |  |
| 45 | `IsImmersivePicker` | `0x595BF0` | 129 | UnwindData |  |
| 46 | `IsQueryCancelAutoplay` | `0x595D10` | 29 | UnwindData |  |
| 51 | `IsTSPerfFlagEnabled` | `0x595DC0` | 280 | UnwindData |  |
| 62 | `SHCreateInfotipControl` | `0x597160` | 236 | UnwindData |  |
| 63 | `SHGetAttributesRequiringElevationFromDataObject` | `0x597260` | 708 | UnwindData |  |
| 66 | `SHInitializeInfotipControl` | `0x597530` | 205 | UnwindData |  |
| 72 | `UnInitDeletedItem` | `0x597700` | 62 | UnwindData |  |
| 81 | `AddCommas` | `0x5986E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `AddCommasExportW` | `0x5986F0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `CheckWinIniForAssocs` | `0x598750` | 1,057 | UnwindData |  |
| 880 | *Ordinal Only* | `0x598B80` | 43 | UnwindData |  |
| 173 | `DeleteItemsInDataObject` | `0x598BC0` | 357 | UnwindData |  |
| 194 | `EnableAndShowWindow` | `0x598DE0` | 63 | UnwindData |  |
| 211 | `FreeThreadIconCache` | `0x598F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `GetDragImageMsg` | `0x598FB0` | 45 | UnwindData |  |
| 215 | `GetFileDescription` | `0x598FF0` | 109 | UnwindData |  |
| 221 | `GetIconLocationFromExt` | `0x599140` | 290 | UnwindData |  |
| 222 | `GetMsgPos` | `0x599270` | 40 | UnwindData |  |
| 225 | `GetSelectionFromSite` | `0x5992A0` | 153 | UnwindData |  |
| 229 | `GetShellItemsAsTextHGLOBAL` | `0x599340` | 523 | UnwindData |  |
| 231 | `GetStockIconIndexAndSystemIL` | `0x599700` | 231 | UnwindData |  |
| 234 | `GetTargetFromMergedFolderIDList` | `0x5998F0` | 147 | UnwindData |  |
| 235 | `GetTargetItemFromMergedFolderIDList` | `0x599A30` | 114 | UnwindData |  |
| 236 | `GetTargetItemFromMergedFolderItem` | `0x599AB0` | 114 | UnwindData |  |
| 238 | `GetThreadIconCache` | `0x599B30` | 266 | UnwindData |  |
| 299 | `Int64ToString` | `0x599CE0` | 635 | UnwindData |  |
| 303 | `InvokeFolderPidl` | `0x599F70` | 196 | UnwindData |  |
| 304 | `IsBlockedFromOpenWithBrowse` | `0x59A040` | 25 | UnwindData |  |
| 309 | `IsExplorerBrowser` | `0x59A060` | 91 | UnwindData |  |
| 310 | `IsExplorerModeBrowser` | `0x59A0D0` | 114 | UnwindData |  |
| 319 | `IsOtherProcessAnExplorer` | `0x59A150` | 112 | UnwindData |  |
| 320 | `IsPathOwnedByCurrentUser` | `0x59A1D0` | 196 | UnwindData |  |
| 325 | `IsWindowInProcess` | `0x59A2A0` | 85 | UnwindData |  |
| 326 | `ItemIsSystemDrive` | `0x59A300` | 105 | UnwindData |  |
| 327 | `LargeIntegerToString` | `0x59A370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 331 | `MenuCharMatch` | `0x59A380` | 171 | UnwindData |  |
| 335 | `ParseField` | `0x59A440` | 443 | UnwindData |  |
| 336 | `ParsePrinterName` | `0x59A610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `ParsePrinterNameEx` | `0x59A620` | 216 | UnwindData |  |
| 340 | `PathComposeWithArgs` | `0x59A700` | 108 | UnwindData |  |
| 368 | `PathSeperateArgs` | `0x59A780` | 211 | UnwindData |  |
| 369 | `QueryCancelAutoPlayMsg` | `0x59A860` | 90 | UnwindData |  |
| 378 | `ReplaceSearchIDListScope` | `0x59A8C0` | 549 | UnwindData |  |
| 390 | `SHBindToObjectByName` | `0x59AAF0` | 132 | UnwindData |  |
| 391 | `SHBindToObjectWithMode` | `0x59AB80` | 126 | UnwindData |  |
| 402 | `SHCreateDataObjectFromShellItemsOrFolder` | `0x59AC10` | 309 | UnwindData |  |
| 431 | `SHEnumerateUnreadMailAccountsW` | `0x59AF40` | 250 | UnwindData |  |
| 436 | `SHFileOperationEx` | `0x59B040` | 412 | UnwindData |  |
| 438 | `SHFindComputer` | `0x59B1F0` | 202 | UnwindData |  |
| 90 | `SHFindFiles` | `0x59B2C0` | 208 | UnwindData |  |
| 750 | *Ordinal Only* | `0x59B3A0` | 378 | UnwindData |  |
| 477 | `SHGetPathFromIDListA` | `0x59B520` | 333 | UnwindData |  |
| 491 | `SHGetUnreadMailCountW` | `0x59B680` | 647 | UnwindData |  |
| 496 | `SHIsFileAvailableOffline` | `0x59B910` | 436 | UnwindData |  |
| 499 | `SHLaunchSearch` | `0x59BAD0` | 247 | UnwindData |  |
| 500 | `SHLoadNonloadedIconOverlayIdentifiers` | `0x59BBD0` | 29 | UnwindData |  |
| 522 | `SHSetUnreadMailCountW` | `0x59BC00` | 555 | UnwindData |  |
| 523 | `SHSettingsChanged` | `0x59BE40` | 97 | UnwindData |  |
| 525 | `SHSimpleIDListFromPath` | `0x59BEB0` | 70 | UnwindData |  |
| 526 | `SHSimulateDropOnClsid` | `0x59BF00` | 153 | UnwindData |  |
| 527 | `SHSysErrorMessageBox` | `0x59BFA0` | 412 | UnwindData |  |
| 529 | `SHTrackPopupMenu` | `0x59C150` | 373 | UnwindData |  |
| 574 | `SVIDFromViewMode` | `0x59C2D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 578 | `SetExplorerServerMode` | `0x59C350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 596 | `Shell_MergeMenus` | `0x59C360` | 845 | UnwindData |  |
| 599 | `ShortSizeFormatExportW` | `0x59C6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `ShowElevationPromptSuppressedError` | `0x59C6E0` | 180 | UnwindData |  |
| 603 | `SimulateDropWithPasteSucceeded` | `0x59C7A0` | 195 | UnwindData |  |
| 612 | `Stream_ReadStringW` | `0x59CA10` | 166 | UnwindData |  |
| 615 | `TransferDelete` | `0x59CBA0` | 316 | UnwindData |  |
| 618 | `ViewModeFromSVID` | `0x59CCF0` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `CreateStorageHandlerViaMoniker` | `0x59D2E0` | 299 | UnwindData |  |
| 25 | `GetShellIconLocationCommaIndex` | `0x59DCF0` | 129 | UnwindData |  |
| 29 | `GetStockIcon` | `0x59DD80` | 120 | UnwindData |  |
| 31 | `GetSystemImageListBitDepth` | `0x59DE00` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `IsIconResourcePath` | `0x59DE90` | 400 | UnwindData |  |
| 50 | `IsShell32IconStock` | `0x59E1F0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `Shell32IconToShell32ExtractIconParameter` | `0x59E230` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `FileIconInitIfNeeded` | `0x59EB80` | 27 | UnwindData |  |
| 429 | `SHDefExtractIconA` | `0x59EC50` | 142 | UnwindData |  |
| 592 | `Shell_GetCachedImageIndex` | `0x59ECF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 593 | `Shell_GetCachedImageIndexA` | `0x59ED00` | 108 | UnwindData |  |
| 595 | `Shell_GetImageLists` | `0x59ED80` | 117 | UnwindData |  |
| 597 | `Shell_SysColorChange` | `0x59EE00` | 179 | UnwindData |  |
| 37 | `IItemCategorizer_SetCategories` | `0x5A1310` | 428 | UnwindData |  |
| 97 | `CAlphabeticalCategorizer_CreateInstance` | `0x5A37A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `CCategorizerFactory_CreateInstance` | `0x5A37C0` | 139 | UnwindData |  |
| 102 | `CCategoryProvider_CreateInstance` | `0x5A3860` | 188 | UnwindData |  |
| 106 | `CDriveSizeCategorizer_CreateInstance` | `0x5A39D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `CDriveTypeCategorizer_CreateInstance` | `0x5A39F0` | 155 | UnwindData |  |
| 117 | `CFreeSpaceCategorizer_CreateInstance` | `0x5A3AA0` | 59 | UnwindData |  |
| 125 | `CPercentCategorizer_CreateInstance` | `0x5A3C70` | 52 | UnwindData |  |
| 128 | `CRatingsCategorizer_CreateInstance` | `0x5A3DB0` | 176 | UnwindData |  |
| 138 | `CSizeCategorizer_CreateInstance` | `0x5A3E70` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `CTimeCategorizer_CreateInstance` | `0x5A4020` | 42 | UnwindData |  |
| 910 | *Ordinal Only* | `0x5A4050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `Install_AdvancedShellSettings` | `0x5A4060` | 69 | UnwindData |  |
| 483 | `SHGetSettings` | `0x5A44C0` | 103 | UnwindData |  |
| 56 | `RealShellExecuteA` | `0x5A6F00` | 8,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `RealShellExecuteExA` | `0x5A6F00` | 8,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `RealShellExecuteExW` | `0x5A6F00` | 8,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `RealShellExecuteW` | `0x5A6F00` | 8,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `SHCreateProcessAsUserW` | `0x5A8EA0` | 29 | UnwindData |  |
| 586 | `ShellExec_RunDLLA` | `0x5A8ED0` | 162 | UnwindData |  |
| 587 | `ShellExec_RunDLLW` | `0x5A8F80` | 343 | UnwindData |  |
| 588 | `ShellExecuteA` | `0x5A90E0` | 132 | UnwindData |  |
| 589 | `ShellExecuteExA` | `0x5A9170` | 218 | UnwindData |  |
| 591 | `ShellExecuteW` | `0x5A9250` | 158 | UnwindData |  |
| 619 | `WOWShellExecute` | `0x5A9300` | 286 | UnwindData |  |
| 61 | `ResolveShortNameCollisions` | `0x5AB100` | 430 | UnwindData |  |
| 141 | `CTaskEnumHKCR_Create` | `0x5AD9D0` | 177 | UnwindData |  |
| 476 | `SHGetNoAssocIconIndex` | `0x5ADA90` | 10,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `VerifySaferTrust` | `0x5B0580` | 460 | UnwindData |  |
| 207 | `FindExecutableA` | `0x5B0C10` | 208 | UnwindData |  |
| 208 | `FindExecutableW` | `0x5B0CF0` | 416 | UnwindData |  |
| 311 | `IsImmersiveUICaller` | `0x5B0EA0` | 190 | UnwindData |  |
| 533 | `SHValidateUNC` | `0x5B0FE0` | 375 | UnwindData |  |
| 583 | `ShellExecCmdLine` | `0x5B1160` | 49 | UnwindData |  |
| 584 | `ShellExecCmdLineWithSite` | `0x5B11A0` | 552 | UnwindData |  |
| 585 | `ShellExecPidl` | `0x5B13D0` | 404 | UnwindData |  |
| 83 | `AddHashItem` | `0x5B1570` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `CreateHashItemTable` | `0x5B1590` | 86 | UnwindData |  |
| 171 | `DeleteHashItem` | `0x5B15F0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | `FindHashItem` | `0x5B16D0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 625 | `_CalculateHashKey` | `0x5B1A50` | 90 | UnwindData |  |
| 91 | `AssocGetPropListForExt` | `0x5B47D0` | 253 | UnwindData |  |
| 441 | `SHGetAssocKeys` | `0x5B48E0` | 337 | UnwindData |  |
| 442 | `SHGetAssocKeysForIDList` | `0x5B4A40` | 132 | UnwindData |  |
| 96 | `BuildUniqueLinkName` | `0x5B6290` | 203 | UnwindData |  |
| 384 | `SHAlloc` | `0x5B64C0` | 39 | UnwindData |  |
| 172 | *Ordinal Only* | `0x5B64F0` | 39 | UnwindData |  |
| 898 | *Ordinal Only* | `0x5B6520` | 413 | UnwindData |  |
| 422 | `SHCreateShellItem` | `0x5B66D0` | 62 | UnwindData |  |
| 446 | `SHGetDataFromIDListA` | `0x5B6720` | 277 | UnwindData |  |
| 447 | `SHGetDataFromIDListW` | `0x5B6840` | 391 | UnwindData |  |
| 449 | `SHGetDiskFreeSpaceExA` | `0x5B69D0` | 115 | UnwindData |  |
| 451 | `SHGetFileIcon` | `0x5B6A50` | 135 | UnwindData |  |
| 452 | `SHGetFileInfoA` | `0x5B6AE0` | 308 | UnwindData |  |
| 463 | `SHGetItemFromDataObject` | `0x5B6C20` | 114 | UnwindData |  |
| 469 | `SHGetLocalizedName` | `0x5B6CA0` | 161 | UnwindData |  |
| 470 | `SHGetLocalizedNameAlloc` | `0x5B6D50` | 235 | UnwindData |  |
| 471 | `SHGetMalloc` | `0x5B6E50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 474 | `SHGetNewLinkInfoA` | `0x5B6E70` | 273 | UnwindData |  |
| 475 | `SHGetNewLinkInfoW` | `0x5B6F90` | 34 | UnwindData |  |
| 243 | *Ordinal Only* | `0x5B6FC0` | 134 | UnwindData |  |
| 244 | *Ordinal Only* | `0x5B7050` | 140 | UnwindData |  |
| 488 | `SHGetTemporaryPropertyForItem` | `0x5B70F0` | 193 | UnwindData |  |
| 501 | `SHMapIDListToSystemImageListIndex` | `0x5B71C0` | 26 | UnwindData |  |
| 513 | `SHRemoveLocalizedName` | `0x5B71E0` | 148 | UnwindData |  |
| 520 | `SHSetLocalizedName` | `0x5B7280` | 243 | UnwindData |  |
| 98 | `CApplyPropertiesUndoUnit_CreateInstance` | `0x5B7EB0` | 134 | UnwindData |  |
| 113 | `CFilterEventSink_CreateInstance` | `0x5B9210` | 185 | UnwindData |  |
| 622 | `WrapSinkAndAdviseCollection` | `0x5B9370` | 184 | UnwindData |  |
| 623 | `WrapSinkAndAdviseItem` | `0x5B9430` | 184 | UnwindData |  |
| 115 | `CFolderInfoTip_CreateInstance` | `0x5BA1B0` | 135 | UnwindData |  |
| 116 | `CFolderShortcut_CreateInstance` | `0x5BDE20` | 121 | UnwindData |  |
| 119 | `CINIPropSetStg_CreateInstance` | `0x5BFA40` | 31 | UnwindData |  |
| 122 | `CItemStoreFilter_CreateInstance` | `0x5C1490` | 13,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `CPinnedPeopleList_CreateInstance` | `0x5C4AE0` | 215 | UnwindData |  |
| 131 | `CSecurityEditor_CreateInstance` | `0x5C6AD0` | 149 | UnwindData |  |
| 137 | `CSidResolver_CreateInstance` | `0x5C6B70` | 207 | UnwindData |  |
| 515 | `SHResolveUserNames` | `0x5C6CF0` | 393 | UnwindData |  |
| 145 | `CheckEscapesW` | `0x5C7020` | 191 | UnwindData |  |
| 338 | `PathAppend` | `0x5C70F0` | 81 | UnwindData |  |
| 341 | `PathFileExists` | `0x5C7150` | 69 | UnwindData |  |
| 343 | `PathGetMountPointFromPath` | `0x5C71A0` | 285 | UnwindData |  |
| 350 | `PathIsExeStub` | `0x5C72D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `PathIsRoot` | `0x5C72E0` | 67 | UnwindData |  |
| 356 | `PathIsSlowA` | `0x5C7330` | 90 | UnwindData |  |
| 357 | `PathIsSlowW` | `0x5C7390` | 145 | UnwindData |  |
| 359 | `PathIsTemporaryA` | `0x5C7430` | 83 | UnwindData |  |
| 362 | `PathMakePretty` | `0x5C7490` | 104 | UnwindData |  |
| 363 | `PathMakeUniqueName` | `0x5C7500` | 39 | UnwindData |  |
| 364 | `PathQualify` | `0x5C7530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `PathQualifyDef` | `0x5C7550` | 825 | UnwindData |  |
| 366 | `PathRemoveFileSpec` | `0x5C7890` | 67 | UnwindData |  |
| 149 | `ConvertStrings` | `0x5C7980` | 348 | UnwindData |  |
| 152 | `CreateDisplayNameRemapTransferSource` | `0x5C9280` | 228 | UnwindData |  |
| 154 | `CreateInfoTipFromItem` | `0x5C9E30` | 36 | UnwindData |  |
| 183 | `DoEnvironmentSubstA` | `0x5CA470` | 161 | UnwindData |  |
| 184 | `DoEnvironmentSubstW` | `0x5CA520` | 163 | UnwindData |  |
| 186 | `DragAcceptFiles` | `0x5CA660` | 78 | UnwindData |  |
| 187 | `DragFinish` | `0x5CA6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 188 | `DragQueryFileA` | `0x5CA6E0` | 28 | UnwindData |  |
| 189 | `DragQueryFileAorW` | `0x5CA710` | 713 | UnwindData |  |
| 190 | `DragQueryFileW` | `0x5CA9E0` | 25 | UnwindData |  |
| 191 | `DragQueryInfo` | `0x5CAA00` | 433 | UnwindData |  |
| 192 | `DragQueryPoint` | `0x5CABC0` | 126 | UnwindData |  |
| 193 | `DuplicateIcon` | `0x5CAC50` | 139 | UnwindData |  |
| 197 | `ExtractAssociatedIconA` | `0x5CACF0` | 249 | UnwindData |  |
| 198 | `ExtractAssociatedIconExA` | `0x5CADF0` | 242 | UnwindData |  |
| 199 | `ExtractAssociatedIconExW` | `0x5CAEF0` | 605 | UnwindData |  |
| 200 | `ExtractAssociatedIconW` | `0x5CB160` | 123 | UnwindData |  |
| 201 | `ExtractIconA` | `0x5CB1F0` | 123 | UnwindData |  |
| 202 | `ExtractIconExA` | `0x5CB280` | 117 | UnwindData |  |
| 203 | `ExtractIconExW` | `0x5CB300` | 534 | UnwindData |  |
| 204 | `ExtractIconW` | `0x5CB520` | 216 | UnwindData |  |
| 435 | `SHExtractIconsW` | `0x5CB740` | 68 | UnwindData |  |
| 274 | `HIDA_ILClone` | `0x5CB790` | 87 | UnwindData |  |
| 278 | `ILAppendID` | `0x5CB7F0` | 266 | UnwindData |  |
| 282 | `ILCreateFromPathA` | `0x5CB900` | 126 | UnwindData |  |
| 284 | `ILCreateFromPathW` | `0x5CB990` | 71 | UnwindData |  |
| 288 | `ILGetDisplayName` | `0x5CB9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `ILGetDisplayNameEx` | `0x5CBA00` | 254 | UnwindData |  |
| 294 | `ILIsParentByPath` | `0x5CBB10` | 313 | UnwindData |  |
| 28 | `SHILCreateFromPath` | `0x5CBC50` | 29 | UnwindData |  |
| 528 | `SHTestTokenPrivilegeW` | `0x5CBDF0` | 184 | UnwindData |  |
| 328 | `LookupFileClassAdorner` | `0x5CC1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 329 | `LookupFileClassTypeOverlay` | `0x5CC1E0` | 22 | UnwindData |  |
| 379 | `ResetFileClassIcon` | `0x5CC200` | 137 | UnwindData |  |
| 579 | `SetFileClassAdorner` | `0x5CC290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 580 | `SetFileClassTypeOverlay` | `0x5CC2B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 333 | `OldReadCabinetState` | `0x5CC2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 372 | `ReadCabinetState` | `0x5CC2E0` | 545 | UnwindData |  |
| 624 | `WriteCabinetState` | `0x5CC510` | 365 | UnwindData |  |
| 473 | `SHGetNetResource` | `0x5CC840` | 397 | UnwindData |  |
| 504 | `SHNetConnectionDialog` | `0x5CC9E0` | 246 | UnwindData |  |
| 382 | `SHAddDefaultPropertiesByExt` | `0x5CCE60` | 177 | UnwindData |  |
| 404 | `SHCreateDefaultPropertiesOp` | `0x5CCF20` | 300 | UnwindData |  |
| 516 | `SHSetDefaultProperties` | `0x5CD060` | 240 | UnwindData |  |
| 887 | *Ordinal Only* | `0x5CDB90` | 297 | UnwindData |  |
| 434 | `SHExtCoCreateLocalServerLowIL` | `0x5CDCC0` | 278 | UnwindData |  |
| 507 | `SHPinDllOfCLSIDStr` | `0x5CDDE0` | 81 | UnwindData |  |
| 398 | `SHCopyStreamWithProgress` | `0x5CDE40` | 25 | UnwindData |  |
| 400 | `SHCreateAssociationRegistration` | `0x5D2D70` | 5,280 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 928 | *Ordinal Only* | `0x5D4210` | 133 | UnwindData |  |
| 439 | `SHFlushSFCache` | `0x5D4300` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `StgMakeUniqueName` | `0x5D4670` | 311 | UnwindData |  |
| 616 | `TryBrokerSHBrowseForFolder` | `0x5D4A10` | 504 | UnwindData |  |
| 298 | `IUnknown_ResolveItem` | `0x5FB920` | 138 | UnwindData |  |
| 576 | `SerializeLinkToText` | `0x5FB9B0` | 293 | UnwindData |  |
| 505 | `SHOpenFolderAndSelectItems` | `0x5FD7A0` | 539 | UnwindData |  |
