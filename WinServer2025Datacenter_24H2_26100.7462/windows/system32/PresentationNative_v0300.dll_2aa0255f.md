# Binary Specification: PresentationNative_v0300.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\PresentationNative_v0300.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2aa0255ff083da3fb406a9ca53549f6785d8fde7eca917eeaad06af96959c01a`
* **Total Exported Functions:** 157

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 212 | `LocbkGetObjectHandlerInfo` | `0x109C` | 1,644 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 334 | `LoCreateContext` | `0x1708` | 581 | UnwindData |  |
| 335 | `LoCreateLine` | `0x1954` | 1,480 | UnwindData |  |
| 336 | `LoCreateParaBreakingSession` | `0x1F24` | 333 | UnwindData |  |
| 340 | `LoDisposeLine` | `0x2078` | 207 | UnwindData |  |
| 333 | `LoCreateBreaks` | `0x2150` | 1,086 | UnwindData |  |
| 341 | `LoDisposeParaBreakingSession` | `0x2594` | 171 | UnwindData |  |
| 348 | `LoRelievePenaltyResource` | `0x2648` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 330 | `LoAcquireBreakRecord` | `0x2664` | 28 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 339 | `LoDisposeBreakRecord` | `0x2680` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 332 | `LoCloneBreakRecord` | `0x268C` | 311 | UnwindData |  |
| 350 | `LoSetDoc` | `0x27CC` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `LoSetTabs` | `0x27DC` | 145 | UnwindData |  |
| 338 | `LoDisplayLine` | `0x2874` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `LoEnumLine` | `0x2884` | 336 | UnwindData |  |
| 346 | `LoQueryLineCpPpoint` | `0x29DC` | 428 | UnwindData |  |
| 347 | `LoQueryLinePointPcp` | `0x2B90` | 38 | UnwindData |  |
| 331 | `LoAcquirePenaltyModule` | `0x2BBC` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `LoDestroyContext` | `0x2BEC` | 41 | UnwindData |  |
| 342 | `LoDisposePenaltyModule` | `0x2BEC` | 41 | UnwindData |  |
| 345 | `LoGetPenaltyModuleInternalHandle` | `0x2C1C` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `LoGetEscString` | `0x2C3C` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `LoSetBreaking` | `0x34EC` | 260 | UnwindData |  |
| 213 | `FsAddFigureObstacle` | `0x5A538` | 126 | UnwindData |  |
| 314 | `FsResolveOverlap` | `0x5A5BC` | 200 | UnwindData |  |
| 252 | `FsGetFigureObstacleData` | `0x5A68C` | 381 | UnwindData |  |
| 249 | `FsGetClientHandle` | `0x5A810` | 116 | UnwindData |  |
| 225 | `FsCreatePageFinite` | `0x5A88C` | 128 | UnwindData |  |
| 329 | `FsUpdateFinitePage` | `0x5A914` | 128 | UnwindData |  |
| 224 | `FsCreatePageBottomless` | `0x5A99C` | 103 | UnwindData |  |
| 325 | `FsUpdateBottomlessPage` | `0x5AA0C` | 107 | UnwindData |  |
| 214 | `FsClearUpdateInfoInPage` | `0x5AA80` | 102 | UnwindData |  |
| 230 | `FsDestroyPage` | `0x5AAEC` | 63 | UnwindData |  |
| 239 | `FsDuplicatePageBreakRecord` | `0x5AB34` | 102 | UnwindData |  |
| 231 | `FsDestroyPageBreakRecord` | `0x5ABA0` | 63 | UnwindData |  |
| 227 | `FsCreateSubpageFinite` | `0x5ABE8` | 563 | UnwindData |  |
| 226 | `FsCreateSubpageBottomless` | `0x5AE24` | 484 | UnwindData |  |
| 326 | `FsUpdateBottomlessSubpage` | `0x5B010` | 473 | UnwindData |  |
| 215 | `FsClearUpdateInfoInSubpage` | `0x5B1F0` | 63 | UnwindData |  |
| 232 | `FsDestroySubpage` | `0x5B238` | 63 | UnwindData |  |
| 240 | `FsDuplicateSubpageBreakRecord` | `0x5B280` | 102 | UnwindData |  |
| 233 | `FsDestroySubpageBreakRecord` | `0x5B2EC` | 63 | UnwindData |  |
| 262 | `FsGetSubpageColumnBalancingInfo` | `0x5B334` | 83 | UnwindData |  |
| 258 | `FsGetNumberSubpageFootnotes` | `0x5B390` | 53 | UnwindData |  |
| 263 | `FsGetSubpageFootnoteInfo` | `0x5B3CC` | 91 | UnwindData |  |
| 219 | `FsCompareSubpages` | `0x5B430` | 99 | UnwindData |  |
| 318 | `FsTransferDisplayInfoSubpage` | `0x5B49C` | 63 | UnwindData |  |
| 270 | `FsJustifySubpage` | `0x5B4E4` | 105 | UnwindData |  |
| 246 | `FsFormatSubtrackFinite` | `0x5B554` | 235 | UnwindData |  |
| 245 | `FsFormatSubtrackBottomless` | `0x5B648` | 208 | UnwindData |  |
| 327 | `FsUpdateBottomlessSubtrack` | `0x5B720` | 209 | UnwindData |  |
| 317 | `FsSynchronizeBottomlessSubtrack` | `0x5B7F8` | 79 | UnwindData |  |
| 216 | `FsClearUpdateInfoInSubtrack` | `0x5B850` | 76 | UnwindData |  |
| 234 | `FsDestroySubtrack` | `0x5B8A4` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `FsDuplicateSubtrackBreakRecord` | `0x5B8B0` | 157 | UnwindData |  |
| 235 | `FsDestroySubtrackBreakRecord` | `0x5B954` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `FsGetSubtrackColumnBalancingInfo` | `0x5B960` | 85 | UnwindData |  |
| 259 | `FsGetNumberSubtrackFootnotes` | `0x5B9BC` | 65 | UnwindData |  |
| 265 | `FsGetSubtrackFootnoteInfo` | `0x5BA04` | 112 | UnwindData |  |
| 316 | `FsShiftSubtrackVertical` | `0x5BA7C` | 332 | UnwindData |  |
| 220 | `FsCompareSubtrack` | `0x5BBD0` | 309 | UnwindData |  |
| 319 | `FsTransferDisplayInfoSubtrack` | `0x5BD0C` | 93 | UnwindData |  |
| 248 | `FsFormatTableSrvFinite` | `0x5BD70` | 530 | UnwindData |  |
| 247 | `FsFormatTableSrvBottomless` | `0x5BF88` | 151 | UnwindData |  |
| 328 | `FsUpdateBottomlessTableSrv` | `0x5C028` | 157 | UnwindData |  |
| 217 | `FsClearUpdateInfoInTableSrv` | `0x5C0CC` | 53 | UnwindData |  |
| 236 | `FsDestroyTableSrv` | `0x5C108` | 53 | UnwindData |  |
| 267 | `FsGetTableSrvColumnBalancingInfo` | `0x5C144` | 99 | UnwindData |  |
| 269 | `FsGetTableSrvNumberFootnotes` | `0x5C1B0` | 63 | UnwindData |  |
| 268 | `FsGetTableSrvFootnoteInfo` | `0x5C1F8` | 105 | UnwindData |  |
| 242 | `FsDuplicateTableSrvBreakRecord` | `0x5C268` | 58 | UnwindData |  |
| 237 | `FsDestroyTableSrvBreakRecord` | `0x5C2A8` | 53 | UnwindData |  |
| 320 | `FsTransferDisplayInfoTableSrv` | `0x5C2E4` | 63 | UnwindData |  |
| 221 | `FsCompareTableSrv` | `0x5C32C` | 78 | UnwindData |  |
| 308 | `FsQueryTableSrvTableDetails` | `0x5C380` | 67 | UnwindData |  |
| 307 | `FsQueryTableSrvRowList` | `0x5C3CC` | 86 | UnwindData |  |
| 306 | `FsQueryTableSrvRowDetails` | `0x5C428` | 96 | UnwindData |  |
| 305 | `FsQueryTableSrvCellList` | `0x5C490` | 124 | UnwindData |  |
| 238 | `FsDuplicateGeometry` | `0x5C514` | 103 | UnwindData |  |
| 315 | `FsRestoreGeometry` | `0x5C584` | 103 | UnwindData |  |
| 313 | `FsReleaseGeometry` | `0x5C5F4` | 98 | UnwindData |  |
| 255 | `FsGetMaxNumberEmptySpaces` | `0x5C65C` | 118 | UnwindData |  |
| 251 | `FsGetEmptySpaces` | `0x5C6D8` | 398 | UnwindData |  |
| 257 | `FsGetNextTick` | `0x5C86C` | 147 | UnwindData |  |
| 218 | `FsCommitFilledRectangle` | `0x5C908` | 107 | UnwindData |  |
| 260 | `FsGetPageRectangle` | `0x5C97C` | 135 | UnwindData |  |
| 250 | `FsGetColumnRectangle` | `0x5CA0C` | 122 | UnwindData |  |
| 256 | `FsGetMaxNumberIntervals` | `0x5CA8C` | 122 | UnwindData |  |
| 254 | `FsGetIntervals` | `0x5CB0C` | 149 | UnwindData |  |
| 312 | `FsRegisterFloatObstacle` | `0x5CBA8` | 107 | UnwindData |  |
| 222 | `FsCreateDocContext` | `0x5CC1C` | 51 | UnwindData |  |
| 228 | `FsDestroyDocContext` | `0x5CC58` | 63 | UnwindData |  |
| 223 | `FsCreateDummyFootnoteRejector` | `0x5CCA0` | 98 | UnwindData |  |
| 229 | `FsDestroyFootnoteRejector` | `0x5CD08` | 61 | UnwindData |  |
| 243 | `FsFAllFootnotesAllowed` | `0x5CD4C` | 146 | UnwindData |  |
| 244 | `FsFFootnoteAllowed` | `0x5CDE4` | 95 | UnwindData |  |
| 253 | `FsGetFloaterFsimethods` | `0x6052C` | 68 | UnwindData |  |
| 277 | `FsQueryFloaterDetails` | `0x60578` | 100 | UnwindData |  |
| 261 | `FsGetShiftOffset` | `0x605E4` | 141 | UnwindData |  |
| 266 | `FsGetTableObjFsimethods` | `0x64480` | 68 | UnwindData |  |
| 299 | `FsQueryTableObjDetails` | `0x644CC` | 150 | UnwindData |  |
| 304 | `FsQueryTableObjTableProperDetails` | `0x64568` | 67 | UnwindData |  |
| 303 | `FsQueryTableObjRowList` | `0x645B4` | 86 | UnwindData |  |
| 302 | `FsQueryTableObjRowDetails` | `0x64610` | 96 | UnwindData |  |
| 298 | `FsQueryTableObjCellList` | `0x64678` | 113 | UnwindData |  |
| 300 | `FsQueryTableObjFigureCountWord` | `0x646F0` | 93 | UnwindData |  |
| 301 | `FsQueryTableObjFigureListWord` | `0x64754` | 80 | UnwindData |  |
| 284 | `FsQueryPageDetails` | `0x647AC` | 673 | UnwindData |  |
| 285 | `FsQueryPageFootnoteColumnList` | `0x64A54` | 291 | UnwindData |  |
| 278 | `FsQueryFootnoteColumnDetails` | `0x64B80` | 102 | UnwindData |  |
| 279 | `FsQueryFootnoteColumnTrackList` | `0x64BEC` | 117 | UnwindData |  |
| 286 | `FsQueryPageSectionList` | `0x64C68` | 328 | UnwindData |  |
| 289 | `FsQuerySectionDetails` | `0x64DB8` | 102 | UnwindData |  |
| 287 | `FsQuerySectionBasicColumnList` | `0x64E24` | 163 | UnwindData |  |
| 290 | `FsQuerySectionEndnoteColumnList` | `0x64ED0` | 163 | UnwindData |  |
| 275 | `FsQueryEndnoteColumnDetails` | `0x64F7C` | 102 | UnwindData |  |
| 288 | `FsQuerySectionCompositeColumnList` | `0x64FE8` | 163 | UnwindData |  |
| 272 | `FsQueryCompositeColumnDetails` | `0x65094` | 130 | UnwindData |  |
| 273 | `FsQueryCompositeColumnFootnoteList` | `0x6511C` | 145 | UnwindData |  |
| 310 | `FsQueryTrackDetails` | `0x651B4` | 148 | UnwindData |  |
| 311 | `FsQueryTrackParaList` | `0x65250` | 117 | UnwindData |  |
| 293 | `FsQuerySubpageDetails` | `0x652CC` | 102 | UnwindData |  |
| 292 | `FsQuerySubpageBasicColumnList` | `0x65338` | 117 | UnwindData |  |
| 296 | `FsQuerySubtrackDetails` | `0x653B4` | 260 | UnwindData |  |
| 297 | `FsQuerySubtrackParaList` | `0x654C0` | 242 | UnwindData |  |
| 309 | `FsQueryTextDetails` | `0x655B8` | 102 | UnwindData |  |
| 282 | `FsQueryLineListComposite` | `0x65624` | 201 | UnwindData |  |
| 283 | `FsQueryLineListSingle` | `0x656F4` | 200 | UnwindData |  |
| 271 | `FsQueryAttachedObjectList` | `0x657C4` | 207 | UnwindData |  |
| 281 | `FsQueryLineCompositeElementList` | `0x6589C` | 130 | UnwindData |  |
| 276 | `FsQueryFigureObjectDetails` | `0x65924` | 102 | UnwindData |  |
| 274 | `FsQueryDcpLineVariantsFromCachedTextPara` | `0x65990` | 117 | UnwindData |  |
| 280 | `FsQueryHeightDefinedColumnSpanAreaList` | `0x65A0C` | 137 | UnwindData |  |
| 291 | `FsQuerySegmentDefinedColumnSpanAreaList` | `0x65A9C` | 137 | UnwindData |  |
| 294 | `FsQuerySubpageHeightDefinedColumnSpanAreaList` | `0x65B2C` | 109 | UnwindData |  |
| 295 | `FsQuerySubpageSegmentDefinedColumnSpanAreaList` | `0x65BA0` | 109 | UnwindData |  |
| 322 | `FsTransformPoint` | `0x65C14` | 156 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `FsTransformVector` | `0x65CB0` | 100 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `FsTransformRectangle` | `0x65D14` | 273 | UnwindData |  |
| 321 | `FsTransformBbox` | `0x65E2C` | 48 | UnwindData |  |
| 353 | `NlCreateHyphenator` | `0xE58D4` | 237 | UnwindData |  |
| 354 | `NlDestroyHyphenator` | `0xE59C8` | 117 | UnwindData |  |
| 356 | `NlHyphenate` | `0xE5A44` | 191 | UnwindData |  |
| 357 | `NlLoad` | `0xE67CC` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 358 | `NlUnload` | `0xE67D8` | 12 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 355 | `NlGetClassObject` | `0xE67E4` | 1,484 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `CreateDocContext` | `0xE6DB0` | 77 | UnwindData |  |
| 208 | `DestroyDocContext` | `0xE6E04` | 24 | UnwindData |  |
| 207 | `CreateInstalledObjectsInfo` | `0xE6E24` | 238 | UnwindData |  |
| 209 | `DestroyInstalledObjectsInfo` | `0xE6F18` | 47 | UnwindData |  |
| 210 | `GetFloaterHandlerInfo` | `0xE6F50` | 46 | UnwindData |  |
| 211 | `GetTableObjHandlerInfo` | `0xE6F84` | 46 | UnwindData |  |
| 352 | `MILGetClassificationTables` | `0xE7058` | 220 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `ums_deflate_init` | `0xE7134` | 43 | UnwindData |  |
| 203 | `ums_deflate` | `0xE75B8` | 2,432 | UnwindData |  |
| 204 | `ums_inflate_init` | `0xE9858` | 273 | UnwindData |  |
| 205 | `ums_inflate` | `0xE9A68` | 5,492 | UnwindData |  |
