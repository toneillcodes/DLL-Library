# Binary Specification: mip_core.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft-Edge-WebView\mip_core.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b91132b09bccc01df0d0a168691bb9e3720d7a5c0f69f1fd838ea6f87cceab0d`
* **Total Exported Functions:** 135

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 57 | `?DecryptBuffer@bufferprotector@mipns@@YA_JAEBVCryptoDelegate@2@W4CipherMode@2@AEBVCryptoKey@2@2_JPEBE3PEAE3_NAEBV?$vector@U?$ByteData@_J@mipns@@V?$allocator@U?$ByteData@_J@mipns@@@std@@@std@@@Z` | `0xA8C0` | 492 | UnwindData |  |
| 58 | `?DecryptBuffer@bufferprotector@mipns@@YA_JAEBVCryptoDelegate@2@W4CipherMode@2@AEBVCryptoKey@2@_JPEBE3PEAE3_N6@Z` | `0xAAB0` | 376 | UnwindData |  |
| 59 | `?EncryptBuffer@bufferprotector@mipns@@YA_JAEBVCryptoDelegate@2@W4CipherMode@2@AEBVCryptoKey@2@2_JPEBE3PEAE3_NAEAV?$vector@V?$vector@EV?$allocator@E@std@@@std@@V?$allocator@V?$vector@EV?$allocator@E@std@@@std@@@2@@std@@@Z` | `0xAC30` | 492 | UnwindData |  |
| 60 | `?EncryptBuffer@bufferprotector@mipns@@YA_JAEBVCryptoDelegate@2@W4CipherMode@2@AEBVCryptoKey@2@_JPEBE3PEAE3_N6@Z` | `0xAE20` | 376 | UnwindData |  |
| 7 | `?CrackBlock@mipns@@YA?AV?$vector@EV?$allocator@E@std@@@std@@AEBVCryptoDelegate@1@AEBV23@I111PEBEIW4RSAPadding@1@W4CryptoHashAlgorithm@1@@Z` | `0xC530` | 272 | UnwindData |  |
| 16 | `?CreateAsymmetricCryptoProvider@mipns@@YA?AV?$shared_ptr@VRsaCryptoProvider@mipns@@@std@@AEBV?$shared_ptr@VCryptoDelegate@mipns@@@3@W4CryptoAlgorithm@1@AEBV?$vector@EV?$allocator@E@std@@@3@I@Z` | `0xC640` | 326 | UnwindData |  |
| 23 | `?CreateCryptoProvider@mipns@@YA?AV?$shared_ptr@VCryptoProvider@mipns@@@std@@AEBVCryptoDelegate@1@W4CipherMode@1@AEBVCryptoKey@1@@Z` | `0xC790` | 520 | UnwindData |  |
| 61 | `?GenerateAESKey@mipns@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEBVCryptoDelegate@1@@Z` | `0xC9A0` | 110 | UnwindData |  |
| 62 | `?GenerateAESKeyAsBytes@mipns@@YA?AV?$vector@EV?$allocator@E@std@@@std@@AEBVCryptoDelegate@1@I@Z` | `0xCA10` | 312 | UnwindData |  |
| 64 | `?GetCryptoDelegate@mipns@@YA?AV?$shared_ptr@VCryptoDelegate@mipns@@@std@@AEBV?$shared_ptr@VMipContext@mipns@@@3@@Z` | `0xCB50` | 301 | UnwindData |  |
| 65 | `?GetHashSize@mipns@@YA_KW4CryptoHashAlgorithm@1@@Z` | `0xCC90` | 142 | UnwindData |  |
| 71 | `?IsValidAesKey@mipns@@YA_NAEBVCryptoKey@1@@Z` | `0xCD20` | 21,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `?Create@OpenSslCryptoDelegateImpl@mipns@@SA?AV?$shared_ptr@VOpenSslCryptoDelegateImpl@mipns@@@std@@XZ` | `0x121B0` | 125 | UnwindData |  |
| 27 | `?CreateDomainFromEmail@mipns@@YA?AV?$shared_ptr@VDomain@mipns@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@@Z` | `0x23B40` | 463 | UnwindData |  |
| 28 | `?CreateDomainFromUrl@mipns@@YA?AV?$shared_ptr@VDomain@mipns@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@@Z` | `0x23D10` | 838 | UnwindData |  |
| 40 | `?CreateHttpDirector@mipns@@YA?AV?$shared_ptr@VHttpDirector@mipns@@@std@@AEBV?$shared_ptr@VMipContext@mipns@@@3@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@AEBVIdentity@1@AEBV?$shared_ptr@VHttpDelegate@mipns@@@3@AEBV?$shared_ptr@VHttpProvider@mipns@@@3@AEBV?$shared_ptr@VTelemetryContext@mipns@@@3@@Z` | `0x27480` | 164 | UnwindData |  |
| 41 | `?CreateHttpRequest@mipns@@YA?AV?$shared_ptr@VHttpRequestBase@mipns@@@std@@AEBVHttpRequestBase@1@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@@Z` | `0x2AB30` | 23 | UnwindData |  |
| 42 | `?CreateHttpRequest@mipns@@YA?AV?$shared_ptr@VHttpRequestBase@mipns@@@std@@W4TransportLayerSecurityMinimumVersion@1@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@W4HttpRequestType@1@1@Z` | `0x2AB50` | 50 | UnwindData |  |
| 55 | `?CreateUri@mipns@@YA?AV?$unique_ptr@VUri@mipns@@U?$default_delete@VUri@mipns@@@std@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@@Z` | `0x2ABB0` | 65 | UnwindData |  |
| 69 | `?GetSanitizedUrl@mipns@@YA?AV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@AEBV23@@Z` | `0x2AC00` | 23 | UnwindData |  |
| 20 | `?CreateAuthRequestTransformer@mipns@@YA?AV?$shared_ptr@VRequestTransformer@mipns@@@std@@AEBV?$shared_ptr@VMipContext@mipns@@@3@AEBVIdentity@1@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@AEBV?$shared_ptr@VAuthDelegate@mipns@@@3@AEBV?$shared_ptr@VAuthChallengeProvider@mipns@@@3@AEBV?$shared_ptr@VHttpProvider@mipns@@@3@@Z` | `0x2BAA0` | 164 | UnwindData |  |
| 46 | `?CreateRedirectRequestTransformer@mipns@@YA?AV?$shared_ptr@VRequestTransformer@mipns@@@std@@AEBV?$shared_ptr@VMipContext@mipns@@@3@AEBVIdentity@1@AEBV?$shared_ptr@VRedirectProvider@mipns@@@3@AEBV?$shared_ptr@VHttpProvider@mipns@@@3@@Z` | `0x2BB50` | 137 | UnwindData |  |
| 1 | `?AddContext@ApiContextStorage@mipns@@SAXV?$shared_ptr@VApiContext@mipns@@@std@@@Z` | `0x2E200` | 152 | UnwindData |  |
| 63 | `?GetContext@ApiContextStorage@mipns@@SA?AV?$shared_ptr@VApiContext@mipns@@@std@@XZ` | `0x2E2A0` | 336 | UnwindData |  |
| 72 | `?RemoveContext@ApiContextStorage@mipns@@SAXV?$shared_ptr@VApiContext@mipns@@@std@@@Z` | `0x2E3F0` | 1,126 | UnwindData |  |
| 66 | `?GetIsPiiAllowed@logger@mipns@@YA_NXZ` | `0x2EB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `?GetLogLevel@logger@mipns@@YA?AW4LogLevel@2@XZ` | `0x2EB90` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `?GetLoggerDelegateInstance@logger@mipns@@YAAEBV?$shared_ptr@VLoggerDelegate@mipns@@@std@@XZ` | `0x2EC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?SetIsPiiAllowed@logger@mipns@@YAX_N@Z` | `0x2EC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `?SetLogLevel@logger@mipns@@YAXW4LogLevel@2@@Z` | `0x2EC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `?SetLoggerDelegateInstance@logger@mipns@@YAXAEBV?$shared_ptr@VLoggerDelegate@mipns@@@std@@@Z` | `0x2EC30` | 57 | UnwindData |  |
| 45 | `?CreatePersistentStore@mipns@@YA?AV?$unique_ptr@VPersistentStore@mipns@@U?$default_delete@VPersistentStore@mipns@@@std@@@std@@AEBV?$shared_ptr@VMipContext@mipns@@@3@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@W4MipComponent@1@1AEBV?$vector@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@@3@33AEBV?$shared_ptr@VStorageDelegate@mipns@@@3@_N@Z` | `0x35710` | 1,577 | UnwindData |  |
| 6 | `?CheckLastErrorAndThrow@mipns@@YAXXZ` | `0x35D40` | 359 | UnwindData |  |
| 74 | `?SetLastError@mipns@@YAXV?$shared_ptr@VDelegateResponseError@mipns@@@std@@@Z` | `0x35F00` | 123 | UnwindData |  |
| 14 | `?Create@Win32CryptoDelegateImpl@mipns@@SA?AV?$shared_ptr@VWin32CryptoDelegateImpl@mipns@@@std@@XZ` | `0x37840` | 122 | UnwindData |  |
| 54 | `?CreateTelemetrySchemaValidator@mipns@@YA?AV?$shared_ptr@VTelemetrySchemaValidator@mipns@@@std@@_N@Z` | `0x3B6F0` | 95 | UnwindData |  |
| 77 | `?SetOneDSHttpDelegate@mipns@@YAXAEBV?$shared_ptr@VHttpDelegate@mipns@@@std@@@Z` | `0x6B7D0` | 166 | UnwindData |  |
| 78 | `?SetOneDSIsTls12Enforced@mipns@@YAX_N@Z` | `0x6B880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?SetOneDSTaskDispatcherDelegate@mipns@@YAXAEBV?$shared_ptr@VTaskDispatcherDelegate@mipns@@@std@@@Z` | `0x6B890` | 166 | UnwindData |  |
| 2 | `?ApplyGlobalAuditCustomSettings@mipns@@YAXAEBV?$map@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@U?$less@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@@std@@@2@@std@@@Z` | `0x6CE30` | 40 | UnwindData |  |
| 3 | `?ApplyGlobalAuditMaskingFilter@mipns@@YAXAEBV?$map@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$vector@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@@2@U?$less@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$vector@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$allocator@V` | `0x6CE60` | 97 | UnwindData |  |
| 4 | `?ApplyGlobalTelemetryCustomSettings@mipns@@YAXAEBV?$map@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@U?$less@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V12@@std@@@2@@std@@@Z` | `0x6CED0` | 20 | UnwindData |  |
| 5 | `?ApplyGlobalTelemetryMaskingFilter@mipns@@YAXAEBV?$map@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$vector@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@@2@U?$less@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$vector@V?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@std@@V?$allocat` | `0x6CEF0` | 97 | UnwindData |  |
| 17 | `?CreateAuditEvent@mipns@@YA?AV?$shared_ptr@VAuditEvent@mipns@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@@Z` | `0x6CF60` | 337 | UnwindData |  |
| 18 | `?CreateAuditManager@mipns@@YA?AV?$shared_ptr@VAuditManager@mipns@@@std@@AEBUDiagnosticConfiguration@1@V?$shared_ptr@VAuditDelegate@mipns@@@3@1@Z` | `0x6D0C0` | 318 | UnwindData |  |
| 19 | `?CreateAuditOnlyEventProperty@mipns@@YA?AV?$shared_ptr@VEventProperty@mipns@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@0@Z` | `0x6D200` | 127 | UnwindData |  |
| 21 | `?CreateAutoTelemetryEvent@mipns@@YA?AV?$unique_ptr@VAutoTelemetryEvent@mipns@@U?$default_delete@VAutoTelemetryEvent@mipns@@@std@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@W4EventLevel@1@AEBV?$shared_ptr@VTelemetryContext@mipns@@@3@AEBV?$shared_ptr@VTelemetryManager@mipns@@@3@@Z` | `0x6D280` | 173 | UnwindData |  |
| 22 | `?CreateAutoTelemetryEvent@mipns@@YA?AV?$unique_ptr@VAutoTelemetryEvent@mipns@@U?$default_delete@VAutoTelemetryEvent@mipns@@@std@@@std@@AEBV?$shared_ptr@VTelemetryEvent@mipns@@@3@AEBV?$shared_ptr@VTelemetryContext@mipns@@@3@AEBV?$shared_ptr@VTelemetryManager@mipns@@@3@@Z` | `0x6D330` | 98 | UnwindData |  |
| 24 | `?CreateDefaultAuditDelegate@mipns@@YA?AV?$shared_ptr@VAuditDelegate@mipns@@@std@@AEBV?$shared_ptr@VOneDSAriaHelper@mipns@@@3@AEBUDiagnosticConfiguration@1@@Z` | `0x6D3A0` | 984 | UnwindData |  |
| 26 | `?CreateDefaultTelemetryDelegate@mipns@@YA?AV?$shared_ptr@VTelemetryDelegate@mipns@@@std@@AEBV?$shared_ptr@VOneDSAriaHelper@mipns@@@3@AEBUDiagnosticConfiguration@1@@Z` | `0x6D780` | 984 | UnwindData |  |
| 29 | `?CreateEmptyAuditDelegate@mipns@@YA?AV?$shared_ptr@VAuditDelegate@mipns@@@std@@XZ` | `0x6DB60` | 81 | UnwindData |  |
| 30 | `?CreateEmptyTelemetryDelegate@mipns@@YA?AV?$shared_ptr@VTelemetryDelegate@mipns@@@std@@XZ` | `0x6DBC0` | 81 | UnwindData |  |
| 31 | `?CreateEventContext@mipns@@YA?AV?$shared_ptr@VEventContext@mipns@@@std@@W4Cloud@1@W4DataBoundary@1@AEBVMipContext@1@@Z` | `0x6DC20` | 315 | UnwindData |  |
| 32 | `?CreateEventFactory@mipns@@YA?AV?$shared_ptr@VDiagnosticEventFactory@mipns@@@std@@XZ` | `0x6E1E0` | 81 | UnwindData |  |
| 33 | `?CreateEventFailureProperties@mipns@@YA?AV?$vector@V?$shared_ptr@VEventProperty@mipns@@@std@@V?$allocator@V?$shared_ptr@VEventProperty@mipns@@@std@@@2@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@00H@Z` | `0x6E770` | 214 | UnwindData |  |
| 34 | `?CreateEventFailureProperties@mipns@@YA?AV?$vector@V?$shared_ptr@VEventProperty@mipns@@@std@@V?$allocator@V?$shared_ptr@VEventProperty@mipns@@@std@@@2@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@00HAEBVError@1@@Z` | `0x6E850` | 196 | UnwindData |  |
| 35 | `?CreateEventFailureProperties@mipns@@YA?AV?$vector@V?$shared_ptr@VEventProperty@mipns@@@std@@V?$allocator@V?$shared_ptr@VEventProperty@mipns@@@std@@@2@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@00HAEBVexception_ptr@3@@Z` | `0x6E920` | 307 | UnwindData |  |
| 36 | `?CreateEventProperty@mipns@@YA?AV?$shared_ptr@VEventProperty@mipns@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@0W4Pii@1@@Z` | `0x6EA60` | 136 | UnwindData |  |
| 37 | `?CreateEventProperty@mipns@@YA?AV?$shared_ptr@VEventProperty@mipns@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@NW4Pii@1@@Z` | `0x6EAF0` | 145 | UnwindData |  |
| 38 | `?CreateEventProperty@mipns@@YA?AV?$shared_ptr@VEventProperty@mipns@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@_JW4Pii@1@@Z` | `0x6EB90` | 144 | UnwindData |  |
| 39 | `?CreateEventProperty@mipns@@YA?AV?$shared_ptr@VEventProperty@mipns@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@_N@Z` | `0x6EC20` | 159 | UnwindData |  |
| 44 | `?CreateOneDSAriaHelper@mipns@@YA?AV?$shared_ptr@VOneDSAriaHelper@mipns@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@AEBUDiagnosticConfiguration@1@AEBV?$shared_ptr@VCloudManager@mipns@@@3@W4LogLevel@1@@Z` | `0x6ECC0` | 1,017 | UnwindData |  |
| 51 | `?CreateTelemetryContext@mipns@@YA?AV?$shared_ptr@VTelemetryContext@mipns@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@0AEBV?$shared_ptr@VEventContext@mipns@@@3@AEBV23@@Z` | `0x6F0C0` | 137 | UnwindData |  |
| 52 | `?CreateTelemetryEvent@mipns@@YA?AV?$shared_ptr@VTelemetryEvent@mipns@@@std@@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@3@W4EventLevel@1@@Z` | `0x6F150` | 334 | UnwindData |  |
| 53 | `?CreateTelemetryManager@mipns@@YA?AV?$shared_ptr@VTelemetryManager@mipns@@@std@@AEBUDiagnosticConfiguration@1@V?$shared_ptr@VTelemetryDelegate@mipns@@@3@1@Z` | `0x6F2A0` | 464 | UnwindData |  |
| 43 | `?CreateMipContext@mipns@@YA?AV?$shared_ptr@VMipContext@mipns@@@std@@AEBV?$shared_ptr@$$CBVMipConfiguration@mipns@@@3@@Z` | `0x73430` | 226 | UnwindData |  |
| 70 | `?IsMipCoreLite@mipns@@YA_NXZ` | `0x74320` | 79,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `?Create@MipContext@mipns@@SA?AV?$shared_ptr@VMipContext@mipns@@@std@@AEBUApplicationInfo@2@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@4@W4LogLevel@2@_NAEBV?$shared_ptr@VLoggerDelegate@mipns@@@4@AEBV?$shared_ptr@UDiagnosticConfiguration@mipns@@@4@@Z` | `0x87A50` | 460 | UnwindData |  |
| 11 | `?Create@MipContext@mipns@@SA?AV?$shared_ptr@VMipContext@mipns@@@std@@AEBV?$shared_ptr@$$CBVMipConfiguration@mipns@@@4@@Z` | `0x87C20` | 23 | UnwindData |  |
| 56 | `?CreateWithCustomFeatureSettings@MipContext@mipns@@SA?AV?$shared_ptr@VMipContext@mipns@@@std@@AEBUApplicationInfo@2@AEBV?$basic_string@DU?$char_traits@D@std@@V?$allocator@D@2@@4@W4LogLevel@2@_NAEBV?$shared_ptr@VLoggerDelegate@mipns@@@4@AEBV?$shared_ptr@UDiagnosticConfiguration@mipns@@@4@AEBV?$map@W4FlightingFeature@mipns@@_NU?$less@W4FlightingFeature@mipns@@@std@@V?$allocator@U?$pair@$$CBW4FlightingFeature@mipns@@_N@std@@@4@@4@@Z` | `0x87C40` | 321 | UnwindData |  |
| 80 | `MIP_CC_CreateDictionary` | `0x8A500` | 505 | UnwindData |  |
| 93 | `MIP_CC_Dictionary_GetEntries` | `0x8A700` | 507 | UnwindData |  |
| 115 | `MIP_CC_ReleaseDictionary` | `0x8A900` | 277 | UnwindData |  |
| 81 | `MIP_CC_CreateHttpDelegate` | `0x8DD80` | 345 | UnwindData |  |
| 95 | `MIP_CC_NotifyHttpDelegateResponse` | `0x8DEE0` | 397 | UnwindData |  |
| 116 | `MIP_CC_ReleaseHttpDelegate` | `0x8E070` | 279 | UnwindData |  |
| 82 | `MIP_CC_CreateLoggerDelegate` | `0x8FA30` | 367 | UnwindData |  |
| 83 | `MIP_CC_CreateLoggerDelegateMessageData` | `0x8FBA0` | 456 | UnwindData |  |
| 117 | `MIP_CC_ReleaseLoggerDelegate` | `0x8FD70` | 279 | UnwindData |  |
| 84 | `MIP_CC_CreateMipContext` | `0x904E0` | 75 | UnwindData |  |
| 85 | `MIP_CC_CreateMipContextWithCustomFeatureSettings` | `0x90530` | 3,392 | UnwindData |  |
| 118 | `MIP_CC_ReleaseMipContext` | `0x91270` | 279 | UnwindData |  |
| 86 | `MIP_CC_CreateProtectionDescriptorFromTemplate` | `0x93C40` | 710 | UnwindData |  |
| 87 | `MIP_CC_CreateProtectionDescriptorFromUserRights` | `0x93F10` | 1,691 | UnwindData |  |
| 88 | `MIP_CC_CreateProtectionDescriptorFromUserRoles` | `0x945B0` | 1,691 | UnwindData |  |
| 96 | `MIP_CC_ProtectionDescriptor_DoesAllowOfflineAccess` | `0x94C50` | 640 | UnwindData |  |
| 97 | `MIP_CC_ProtectionDescriptor_DoesContentExpire` | `0x94ED0` | 640 | UnwindData |  |
| 98 | `MIP_CC_ProtectionDescriptor_GetContentId` | `0x95150` | 765 | UnwindData |  |
| 99 | `MIP_CC_ProtectionDescriptor_GetContentValidUntil` | `0x95450` | 662 | UnwindData |  |
| 100 | `MIP_CC_ProtectionDescriptor_GetDescription` | `0x956F0` | 668 | UnwindData |  |
| 101 | `MIP_CC_ProtectionDescriptor_GetDescriptionSize` | `0x95990` | 769 | UnwindData |  |
| 102 | `MIP_CC_ProtectionDescriptor_GetDoubleKeyUrl` | `0x95CA0` | 671 | UnwindData |  |
| 103 | `MIP_CC_ProtectionDescriptor_GetDoubleKeyUrlSize` | `0x95F40` | 772 | UnwindData |  |
| 104 | `MIP_CC_ProtectionDescriptor_GetEncryptedAppData` | `0x96250` | 582 | UnwindData |  |
| 105 | `MIP_CC_ProtectionDescriptor_GetLabelId` | `0x964A0` | 702 | UnwindData |  |
| 106 | `MIP_CC_ProtectionDescriptor_GetName` | `0x96760` | 668 | UnwindData |  |
| 107 | `MIP_CC_ProtectionDescriptor_GetNameSize` | `0x96A00` | 769 | UnwindData |  |
| 108 | `MIP_CC_ProtectionDescriptor_GetOwner` | `0x96D10` | 668 | UnwindData |  |
| 109 | `MIP_CC_ProtectionDescriptor_GetOwnerSize` | `0x96FB0` | 769 | UnwindData |  |
| 110 | `MIP_CC_ProtectionDescriptor_GetProtectionType` | `0x972C0` | 761 | UnwindData |  |
| 111 | `MIP_CC_ProtectionDescriptor_GetReferrer` | `0x975C0` | 668 | UnwindData |  |
| 112 | `MIP_CC_ProtectionDescriptor_GetReferrerSize` | `0x97860` | 769 | UnwindData |  |
| 113 | `MIP_CC_ProtectionDescriptor_GetSignedAppData` | `0x97B70` | 582 | UnwindData |  |
| 114 | `MIP_CC_ProtectionDescriptor_GetTemplateId` | `0x97DC0` | 765 | UnwindData |  |
| 119 | `MIP_CC_ReleaseProtectionDescriptor` | `0x980C0` | 279 | UnwindData |  |
| 89 | `MIP_CC_CreateStream` | `0x98AF0` | 518 | UnwindData |  |
| 120 | `MIP_CC_ReleaseStream` | `0x98D00` | 277 | UnwindData |  |
| 90 | `MIP_CC_CreateStringList` | `0x99440` | 510 | UnwindData |  |
| 121 | `MIP_CC_ReleaseStringList` | `0x99640` | 277 | UnwindData |  |
| 124 | `MIP_CC_StringList_GetStrings` | `0x99760` | 507 | UnwindData |  |
| 91 | `MIP_CC_CreateTaskDispatcherDelegate` | `0x9ACE0` | 367 | UnwindData |  |
| 94 | `MIP_CC_ExecuteDispatchedTask` | `0x9AE50` | 394 | UnwindData |  |
| 122 | `MIP_CC_ReleaseTaskDispatcherDelegate` | `0x9AFE0` | 279 | UnwindData |  |
| 92 | `MIP_CC_CreateTelemetryConfiguration` | `0x9B440` | 240 | UnwindData |  |
| 123 | `MIP_CC_ReleaseTelemetryConfiguration` | `0x9B530` | 279 | UnwindData |  |
| 125 | `MIP_CC_TelemetryConfiguration_AddMaskedProperty` | `0x9B650` | 1,028 | UnwindData |  |
| 126 | `MIP_CC_TelemetryConfiguration_SetCustomSettings` | `0x9BA60` | 649 | UnwindData |  |
| 127 | `MIP_CC_TelemetryConfiguration_SetHostName` | `0x9BCF0` | 632 | UnwindData |  |
| 128 | `MIP_CC_TelemetryConfiguration_SetHttpDelegate` | `0x9BF70` | 1,025 | UnwindData |  |
| 129 | `MIP_CC_TelemetryConfiguration_SetIsFastShutdownEnabled` | `0x9C380` | 525 | UnwindData |  |
| 130 | `MIP_CC_TelemetryConfiguration_SetIsLocalCachingEnabled` | `0x9C590` | 525 | UnwindData |  |
| 131 | `MIP_CC_TelemetryConfiguration_SetIsNetworkDetectionEnabled` | `0x9C7A0` | 525 | UnwindData |  |
| 132 | `MIP_CC_TelemetryConfiguration_SetIsTelemetryOptedOut` | `0x9C9B0` | 525 | UnwindData |  |
| 133 | `MIP_CC_TelemetryConfiguration_SetIsTraceLoggingEnabled` | `0x9CBC0` | 525 | UnwindData |  |
| 134 | `MIP_CC_TelemetryConfiguration_SetLibraryName` | `0x9CDD0` | 633 | UnwindData |  |
| 135 | `MIP_CC_TelemetryConfiguration_SetTaskDispatcherDelegate` | `0x9D050` | 1,041 | UnwindData |  |
| 47 | `?CreateStreamFromBuffer@mipns@@YA?AV?$shared_ptr@VStream@mipns@@@std@@PEAE_J@Z` | `0x9EF90` | 144 | UnwindData |  |
| 48 | `?CreateStreamFromStdStream@mipns@@YA?AV?$shared_ptr@VStream@mipns@@@std@@AEBV?$shared_ptr@V?$basic_iostream@DU?$char_traits@D@std@@@std@@@3@@Z` | `0x9F020` | 127 | UnwindData |  |
| 49 | `?CreateStreamFromStdStream@mipns@@YA?AV?$shared_ptr@VStream@mipns@@@std@@AEBV?$shared_ptr@V?$basic_istream@DU?$char_traits@D@std@@@std@@@3@@Z` | `0x9F0A0` | 127 | UnwindData |  |
| 50 | `?CreateStreamFromStdStream@mipns@@YA?AV?$shared_ptr@VStream@mipns@@@std@@AEBV?$shared_ptr@V?$basic_ostream@DU?$char_traits@D@std@@@std@@@3@@Z` | `0x9F120` | 127 | UnwindData |  |
| 9 | `?Create@JsonDelegateImpl@mipns@@SA?AV?$shared_ptr@VJsonDelegateImpl@mipns@@@std@@XZ` | `0xA26C0` | 122 | UnwindData |  |
| 25 | `?CreateDefaultLoggerDelegate@logger@mipns@@YA?AV?$shared_ptr@VLoggerDelegate@mipns@@@std@@AEBULoggerConfiguration@2@@Z` | `0xAAD30` | 23 | UnwindData |  |
| 15 | `?Create@XmlDelegateImpl@xml@mipns@@SA?AV?$shared_ptr@VXmlDelegateImpl@xml@mipns@@@std@@XZ` | `0xB23E0` | 86 | UnwindData |  |
| 13 | `?Create@StorageDelegateImpl@mipns@@SA?AV?$shared_ptr@VStorageDelegate@mipns@@@std@@AEBVStorageSettings@StorageDelegate@2@@Z` | `0xB7550` | 122 | UnwindData |  |
| 8 | `?Create@HttpClient@mipns@@SA?AV?$shared_ptr@VHttpClient@mipns@@@std@@XZ` | `0xC43B0` | 77 | UnwindData |  |
