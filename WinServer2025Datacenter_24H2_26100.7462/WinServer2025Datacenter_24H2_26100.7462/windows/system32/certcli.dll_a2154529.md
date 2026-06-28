# Binary Specification: certcli.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\certcli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a2154529e64eae5df2ce87adb167e134615dc865447e466805b99e411c012228`
* **Total Exported Functions:** 172

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 371 | `AddOrRemoveOCSPISAPIExtension` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#851` |
| 209 | `CAAccessCheck` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAAccessCheck` |
| 211 | `CAAccessCheckEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAAccessCheckEx` |
| 212 | `CAAddCACertificateType` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAAddCACertificateType` |
| 222 | `CAAddCACertificateTypeEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAAddCACertificateTypeEx` |
| 224 | `CACertTypeAccessCheck` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACertTypeAccessCheck` |
| 226 | `CACertTypeAccessCheckEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACertTypeAccessCheckEx` |
| 227 | `CACertTypeAuthzAccessCheck` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACertTypeAuthzAccessCheck` |
| 228 | `CACertTypeGetSecurity` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACertTypeGetSecurity` |
| 229 | `CACertTypeQuery` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACertTypeQuery` |
| 230 | `CACertTypeRegisterQuery` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACertTypeRegisterQuery` |
| 231 | `CACertTypeSetSecurity` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACertTypeSetSecurity` |
| 232 | `CACertTypeUnregisterQuery` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACertTypeUnregisterQuery` |
| 233 | `CACloneCertType` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACloneCertType` |
| 234 | `CACloseCA` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACloseCA` |
| 235 | `CACloseCertType` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACloseCertType` |
| 236 | `CACountCAs` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACountCAs` |
| 237 | `CACountCertTypes` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACountCertTypes` |
| 238 | `CACreateAutoEnrollmentObjectEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACreateAutoEnrollmentObjectEx` |
| 239 | `CACreateCertType` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACreateCertType` |
| 243 | `CACreateLocalAutoEnrollmentObject` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACreateLocalAutoEnrollmentObject` |
| 244 | `CACreateNewCA` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CACreateNewCA` |
| 268 | `CADCSetCertTypePropertyEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CADCSetCertTypePropertyEx` |
| 269 | `CADeleteCA` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CADeleteCA` |
| 270 | `CADeleteCAEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CADeleteCAEx` |
| 271 | `CADeleteCertType` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CADeleteCertType` |
| 272 | `CADeleteCertTypeEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CADeleteCertTypeEx` |
| 273 | `CADeleteLocalAutoEnrollmentObject` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CADeleteLocalAutoEnrollmentObject` |
| 274 | `CAEnumCertTypes` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAEnumCertTypes` |
| 275 | `CAEnumCertTypesEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAEnumCertTypesEx` |
| 276 | `CAEnumCertTypesForCA` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAEnumCertTypesForCA` |
| 277 | `CAEnumCertTypesForCAEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAEnumCertTypesForCAEx` |
| 278 | `CAEnumFirstCA` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAEnumFirstCA` |
| 279 | `CAEnumNextCA` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAEnumNextCA` |
| 280 | `CAEnumNextCertType` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAEnumNextCertType` |
| 281 | `CAFindByCertType` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAFindByCertType` |
| 282 | `CAFindByIssuerDN` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAFindByIssuerDN` |
| 283 | `CAFindByName` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAFindByName` |
| 284 | `CAFindCertTypeByName` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAFindCertTypeByName` |
| 285 | `CAFreeCAProperty` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAFreeCAProperty` |
| 286 | `CAFreeCertTypeExtensions` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAFreeCertTypeExtensions` |
| 287 | `CAFreeCertTypeProperty` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAFreeCertTypeProperty` |
| 361 | `CAGetAccessRights` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#843` |
| 288 | `CAGetCACertificate` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCACertificate` |
| 289 | `CAGetCAExpiration` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCAExpiration` |
| 290 | `CAGetCAFlags` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCAFlags` |
| 291 | `CAGetCAProperty` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCAProperty` |
| 292 | `CAGetCASecurity` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCASecurity` |
| 363 | `CAGetCertTypeAccessRights` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#845` |
| 293 | `CAGetCertTypeExpiration` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCertTypeExpiration` |
| 294 | `CAGetCertTypeExtensions` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCertTypeExtensions` |
| 295 | `CAGetCertTypeExtensionsEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCertTypeExtensionsEx` |
| 296 | `CAGetCertTypeFlags` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCertTypeFlags` |
| 297 | `CAGetCertTypeFlagsEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCertTypeFlagsEx` |
| 298 | `CAGetCertTypeKeySpec` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCertTypeKeySpec` |
| 299 | `CAGetCertTypeProperty` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCertTypeProperty` |
| 300 | `CAGetCertTypePropertyEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetCertTypePropertyEx` |
| 301 | `CAGetDN` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAGetDN` |
| 302 | `CAInstallDefaultCertType` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAInstallDefaultCertType` |
| 303 | `CAInstallDefaultCertTypeEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAInstallDefaultCertTypeEx` |
| 304 | `CAIsCertTypeCurrent` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAIsCertTypeCurrent` |
| 305 | `CAIsCertTypeCurrentEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAIsCertTypeCurrentEx` |
| 364 | `CAIsCertTypeValid` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#846` |
| 362 | `CAIsValid` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#844` |
| 306 | `CAOIDAdd` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDAdd` |
| 307 | `CAOIDAddEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDAddEx` |
| 308 | `CAOIDCreateNew` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDCreateNew` |
| 309 | `CAOIDCreateNewEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDCreateNewEx` |
| 310 | `CAOIDDelete` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDDelete` |
| 311 | `CAOIDDeleteEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDDeleteEx` |
| 312 | `CAOIDFreeLdapURL` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDFreeLdapURL` |
| 313 | `CAOIDFreeProperty` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDFreeProperty` |
| 314 | `CAOIDGetLdapURL` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDGetLdapURL` |
| 315 | `CAOIDGetProperty` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDGetProperty` |
| 316 | `CAOIDGetPropertyEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDGetPropertyEx` |
| 317 | `CAOIDSetProperty` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDSetProperty` |
| 318 | `CAOIDSetPropertyEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAOIDSetPropertyEx` |
| 319 | `CARemoveCACertificateType` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CARemoveCACertificateType` |
| 320 | `CARemoveCACertificateTypeEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CARemoveCACertificateTypeEx` |
| 321 | `CASetCACertificate` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCACertificate` |
| 322 | `CASetCAExpiration` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCAExpiration` |
| 323 | `CASetCAFlags` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCAFlags` |
| 324 | `CASetCAProperty` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCAProperty` |
| 325 | `CASetCASecurity` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCASecurity` |
| 326 | `CASetCertTypeExpiration` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCertTypeExpiration` |
| 327 | `CASetCertTypeExtension` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCertTypeExtension` |
| 328 | `CASetCertTypeFlags` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCertTypeFlags` |
| 329 | `CASetCertTypeFlagsEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCertTypeFlagsEx` |
| 330 | `CASetCertTypeKeySpec` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCertTypeKeySpec` |
| 331 | `CASetCertTypeProperty` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCertTypeProperty` |
| 332 | `CASetCertTypePropertyEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CASetCertTypePropertyEx` |
| 333 | `CAUpdateCA` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAUpdateCA` |
| 334 | `CAUpdateCAEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAUpdateCAEx` |
| 335 | `CAUpdateCertType` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAUpdateCertType` |
| 336 | `CAUpdateCertTypeEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.CAUpdateCertTypeEx` |
| 201 | `CSPrintAssert` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#701` |
| 202 | `CSPrintError` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#702` |
| 357 | `CSPrintErrorLineFile` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#839` |
| 358 | `CSPrintErrorLineFile2` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#840` |
| 359 | `CSPrintErrorLineFileData` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#841` |
| 360 | `CSPrintErrorLineFileData2` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#842` |
| 390 | `CertcliGetDetailedCertcliVersionString` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#858` |
| 205 | `DbgIsSSActive` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#705` |
| 242 | `DbgLogStringInit` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#811` |
| 366 | `DbgLogStringInit2` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#847` |
| 203 | `DbgPrintf` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#703` |
| 204 | `DbgPrintfInit` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#704` |
| 261 | `DbgPrintfW` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#824` |
| 223 | `DecodeFileW` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#808` |
| 263 | `EnableASPInIIS` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#826` |
| 265 | `EnableISAPIExtension` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#828` |
| 225 | `EncodeToFileW` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#809` |
| 262 | `IsASPEnabledInIIS` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#825` |
| 267 | `IsASPEnabledInIIS_New` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#830` |
| 264 | `IsISAPIExtensionEnabled` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#827` |
| 368 | `RemoveISAPIExtension` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#848` |
| 369 | `RemoveVDir` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#849` |
| 370 | `SplitConfigString` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#850` |
| 246 | `WszToMultiByteInteger` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#813` |
| 245 | `WszToMultiByteIntegerBuf` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#812` |
| 253 | `caTranslateFileTimePeriodToPeriodUnits` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#820` |
| 240 | `myAddShare` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#810` |
| 249 | `myCAPropGetDisplayName` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#816` |
| 251 | `myCAPropInfoLookup` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#818` |
| 250 | `myCAPropInfoUnmarshal` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#817` |
| 254 | `myCryptBinaryToString` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#602` |
| 255 | `myCryptBinaryToStringA` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#604` |
| 256 | `myCryptStringToBinary` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#601` |
| 257 | `myCryptStringToBinaryA` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#603` |
| 342 | `myDoesDSExist@209` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#801` |
| 392 | `myEnablePrivilege` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#855` |
| 213 | `myFreeColumnDisplayNames` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#802` |
| 354 | `myGenerateGuidSerialNumber` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#836` |
| 353 | `myGenerateGuidString` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#835` |
| 207 | `myGetErrorMessageText` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#707` |
| 247 | `myGetErrorMessageText1` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#814` |
| 248 | `myGetErrorMessageTextEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#815` |
| 391 | `myGetHashAlgorithmOIDInfoFromSignatureAlgorithm` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#854` |
| 266 | `myGetSidFromDomain` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#829` |
| 373 | `myGetTargetMachineDomainDnsName` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#852` |
| 216 | `myHExceptionCode` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#805` |
| 260 | `myHExceptionCodePrint` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#823` |
| 356 | `myHGetLastError` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#838` |
| 208 | `myHResultToStringRaw_old` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#708` |
| 206 | `myHResultToString_old` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#706` |
| 215 | `myIsDelayLoadHResult` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#804` |
| 217 | `myJetHResult` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#806` |
| 259 | `myLogExceptionInit` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#822` |
| 218 | `myModifyVirtualRootsAndFileShares` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#807` |
| 375 | `myNetLogonUser` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#853` |
| 258 | `myOIDHashOIDToString` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#821` |
| 352 | `myRevertSanitizeName` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#834` |
| 214 | `myRobustLdapBind` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#803` |
| 252 | `myRobustLdapBindEx` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#819` |
| 349 | `mySanitizeName` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#831` |
| 350 | `mySanitizedNameToDSName` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#832` |
| 351 | `mySanitizedNameToShortName` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#833` |
| 355 | `mylstrcmpiL` | `0x0` | - | Forwarded | Forwarded to: `CERTCA.#837` |
| 337 | `DllCanUnloadNow` | `0xA340` | 50 | UnwindData |  |
| 338 | `DllGetClassObject` | `0xA380` | 120 | UnwindData |  |
| 339 | `DllMain` | `0xA400` | 252 | UnwindData |  |
| 340 | `DllRegisterServer` | `0xA510` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `DllUnregisterServer` | `0xA510` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 491 | `CAGetConfigStringFromUIPicker` | `0xA740` | 126 | UnwindData |  |
| 210 | *Ordinal Only* | `0xE390` | 211 | UnwindData |  |
| 221 | *Ordinal Only* | `0x139E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | *Ordinal Only* | `0x13A00` | 125 | UnwindData |  |
| 219 | *Ordinal Only* | `0x13A90` | 136 | UnwindData |  |
| 374 | *Ordinal Only* | `0x13B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | *Ordinal Only* | `0x13B30` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | *Ordinal Only* | `0x13D20` | 24,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 367 | *Ordinal Only* | `0x19C60` | 1,371 | UnwindData |  |
