# Binary Specification: oneds.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft-Edge-WebView\oneds.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0982403d09d516a5823d73ee9f548946dafa32ab171f05e8bc4a85bc18a08443`
* **Total Exported Functions:** 275

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 254 | `?clear@EventProperty@Events@Applications@Microsoft@@QEAAXXZ` | `0xA3B0` | 242 | UnwindData |  |
| 212 | `?SetLevel@EventProperties@Events@Applications@Microsoft@@QEAAXE@Z` | `0x25AA0` | 115 | UnwindData |  |
| 195 | `?SetAppExperimentETag@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x2C340` | 147 | UnwindData |  |
| 248 | `?SetUserId@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@W4PiiKind@234@@Z` | `0x2C430` | 146 | UnwindData |  |
| 44 | `??0GUID_t@Events@Applications@Microsoft@@QEAA@U_GUID@@@Z` | `0x2FBE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `?copydata@EventProperty@Events@Applications@Microsoft@@AEAAXPEBU1234@@Z` | `0x2FC00` | 442 | UnwindData |  |
| 22 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@AEBU0123@@Z` | `0x2FE80` | 67 | UnwindData |  |
| 98 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@AEBU0123@@Z` | `0x2FF20` | 60 | UnwindData |  |
| 80 | `??1EventProperty@Events@Applications@Microsoft@@UEAA@XZ` | `0x2FF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@XZ` | `0x2FF70` | 66 | UnwindData |  |
| 32 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@PEBDW4PiiKind@123@W4DataCategory@123@@Z` | `0x2FFC0` | 108 | UnwindData |  |
| 23 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@AEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@W4PiiKind@123@W4DataCategory@123@@Z` | `0x30030` | 117 | UnwindData |  |
| 36 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@_JW4PiiKind@123@W4DataCategory@123@@Z` | `0x300B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@NW4PiiKind@123@W4DataCategory@123@@Z` | `0x300E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@_NW4PiiKind@123@W4DataCategory@123@@Z` | `0x30110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `?empty@EventProperty@Events@Applications@Microsoft@@QEAA_NXZ` | `0x30130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `?to_string@EventProperty@Events@Applications@Microsoft@@UEBA?AV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@XZ` | `0x30150` | 1,540 | UnwindData |  |
| 240 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@_JW4PiiKind@234@W4DataCategory@234@@Z` | `0x30BD0` | 104 | UnwindData |  |
| 261 | `?stateLock@DebugEventSource@Events@Applications@Microsoft@@KAAEAVrecursive_mutex@__Cr@std@@XZ` | `0x30C40` | 112 | UnwindData |  |
| 79 | `??1EventProperties@Events@Applications@Microsoft@@UEAA@XZ` | `0x30CE0` | 54 | UnwindData |  |
| 16 | `??0EventProperties@Events@Applications@Microsoft@@QEAA@XZ` | `0x30D20` | 100 | UnwindData |  |
| 14 | `??0EventProperties@Events@Applications@Microsoft@@QEAA@AEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@E@Z` | `0x30DC0` | 245 | UnwindData |  |
| 213 | `?SetName@EventProperties@Events@Applications@Microsoft@@QEAA_NAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x30EF0` | 177 | UnwindData |  |
| 11 | `??0EventProperties@Events@Applications@Microsoft@@QEAA@AEBV0123@@Z` | `0x30FE0` | 63 | UnwindData |  |
| 176 | `?GetLatency@EventProperties@Events@Applications@Microsoft@@QEBA?AW4EventLatency@234@XZ` | `0x311B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 180 | `?GetPersistence@EventProperties@Events@Applications@Microsoft@@QEBA?AW4EventPersistence@234@XZ` | `0x311C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?GetPopSample@EventProperties@Events@Applications@Microsoft@@QEBANXZ` | `0x311D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `?SetPolicyBitFlags@EventProperties@Events@Applications@Microsoft@@QEAAX_K@Z` | `0x311E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 182 | `?GetPolicyBitFlags@EventProperties@Events@Applications@Microsoft@@QEBA_KXZ` | `0x311F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 179 | `?GetName@EventProperties@Events@Applications@Microsoft@@QEBAAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@XZ` | `0x31200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 187 | `?GetType@EventProperties@Events@Applications@Microsoft@@QEBAAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@XZ` | `0x31210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `?GetProperties@EventProperties@Events@Applications@Microsoft@@QEBAAEBV?$map@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UEventProperty@Events@Applications@Microsoft@@U?$less@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UEventProperty@Events@Applications@Microsoft@@@__Cr@std@@@23@@__Cr@std@@W4DataCategory@234@@Z` | `0x31220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UEventProperty@234@@Z` | `0x31240` | 188 | UnwindData |  |
| 236 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@PEBDW4PiiKind@234@W4DataCategory@234@@Z` | `0x31330` | 104 | UnwindData |  |
| 224 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@0W4PiiKind@234@W4DataCategory@234@@Z` | `0x313A0` | 104 | UnwindData |  |
| 235 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@NW4PiiKind@234@W4DataCategory@234@@Z` | `0x31410` | 101 | UnwindData |  |
| 242 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@_NW4PiiKind@234@W4DataCategory@234@@Z` | `0x31480` | 104 | UnwindData |  |
| 159 | `?AddEventListener@DebugEventSource@Events@Applications@Microsoft@@UEAAXW4DebugEventType@234@AEAVDebugEventListener@234@@Z` | `0x32410` | 177 | UnwindData |  |
| 168 | `?DispatchEvent@DebugEventSource@Events@Applications@Microsoft@@UEAA_NVDebugEvent@234@@Z` | `0x324F0` | 371 | UnwindData |  |
| 140 | `??DILogConfiguration@Events@Applications@Microsoft@@QEAAAEAV?$map@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@VVariant@Events@Applications@Microsoft@@U?$less@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@VVariant@Events@Applications@Microsoft@@@__Cr@std@@@23@@__Cr@std@@XZ` | `0x41780` | 4,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `??0ILogConfiguration@Events@Applications@Microsoft@@QEAA@AEBV?$initializer_list@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@VVariant@Events@Applications@Microsoft@@@__Cr@std@@@std@@@Z` | `0x42830` | 92 | UnwindData |  |
| 177 | `?GetModule@ILogConfiguration@Events@Applications@Microsoft@@QEAA?AV?$shared_ptr@VIModule@Events@Applications@Microsoft@@@__Cr@std@@PEBD@Z` | `0x42900` | 306 | UnwindData |  |
| 188 | `?HasConfig@ILogConfiguration@Events@Applications@Microsoft@@QEAA_NPEBD@Z` | `0x42AD0` | 133 | UnwindData |  |
| 139 | `??AILogConfiguration@Events@Applications@Microsoft@@QEAAAEAVVariant@123@PEBD@Z` | `0x42B60` | 142 | UnwindData |  |
| 273 | `GetDecodeDebugEventBufferFunc` | `0x122B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 268 | `CreateEventListenerService` | `0x122B90` | 69 | UnwindData |  |
| 269 | `CreateOneDSWrapper` | `0x123520` | 62 | UnwindData |  |
| 267 | `CreateCommonSchemaHelper` | `0x1243A0` | 50 | UnwindData |  |
| 198 | `?SetAppId@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x124CB0` | 131 | UnwindData |  |
| 201 | `?SetAppVersion@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x124D90` | 131 | UnwindData |  |
| 199 | `?SetAppLanguage@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x124E70` | 131 | UnwindData |  |
| 206 | `?SetDeviceId@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x124F50` | 131 | UnwindData |  |
| 207 | `?SetDeviceMake@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x125030` | 131 | UnwindData |  |
| 208 | `?SetDeviceModel@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x125110` | 131 | UnwindData |  |
| 205 | `?SetDeviceClass@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x1251F0` | 131 | UnwindData |  |
| 214 | `?SetNetworkCost@ISemanticContext@Events@Applications@Microsoft@@UEAAXW4NetworkCost@234@@Z` | `0x1252D0` | 202 | UnwindData |  |
| 215 | `?SetNetworkProvider@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x1253F0` | 129 | UnwindData |  |
| 216 | `?SetNetworkType@ISemanticContext@Events@Applications@Microsoft@@UEAAXW4NetworkType@234@@Z` | `0x1254D0` | 202 | UnwindData |  |
| 218 | `?SetOsName@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x1255F0` | 131 | UnwindData |  |
| 219 | `?SetOsVersion@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x1256D0` | 131 | UnwindData |  |
| 217 | `?SetOsBuild@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x1257B0` | 131 | UnwindData |  |
| 249 | `?SetUserLanguage@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x125890` | 131 | UnwindData |  |
| 251 | `?SetUserTimeZone@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x125970` | 131 | UnwindData |  |
| 202 | `?SetCommercialId@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x125A50` | 129 | UnwindData |  |
| 83 | `??1ILogConfiguration@Events@Applications@Microsoft@@QEAA@XZ` | `0x125B30` | 67 | UnwindData |  |
| 77 | `??1DebugEventSource@Events@Applications@Microsoft@@UEAA@XZ` | `0x125CB0` | 81 | UnwindData |  |
| 220 | `?SetPersistence@EventProperties@Events@Applications@Microsoft@@QEAAXW4EventPersistence@234@@Z` | `0x125D30` | 17,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `?AttachEventSource@DebugEventSource@Events@Applications@Microsoft@@UEAA_NAEAV1234@@Z` | `0x12A260` | 102 | UnwindData |  |
| 172 | `?Get@LogManagerProvider@Events@Applications@Microsoft@@CAPEAVILogManager@234@AEAVILogConfiguration@234@AEAW4status_t@234@@Z` | `0x12A3F0` | 45 | UnwindData |  |
| 191 | `?Release@LogManagerProvider@Events@Applications@Microsoft@@SA?AW4status_t@234@AEAVILogConfiguration@234@@Z` | `0x12A420` | 35 | UnwindData |  |
| 90 | `??4DebugEventDispatcher@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `??4DebugEventListener@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `??4EventListenerService@telemetry_client@@QEAAAEAV01@AEBV01@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `??4IAuthTokensController@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `??4IHttpResponseCallback@telemetry_client@@QEAAAEAV01@AEBV01@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `??4ILogController@Events@Applications@Microsoft@@QEAAAEAV0123@$$QEAV0123@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `??4ILogController@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `??4ILogManager@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `??4ILogger@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `??4IModule@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `??4ISemanticContext@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `??4LogManagerProvider@Events@Applications@Microsoft@@QEAAAEAV0123@$$QEAV0123@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `??4LogManagerProvider@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `??4OneDSWrapper@data_client@@QEAAAEAV01@AEBV01@@Z` | `0x137690` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `??1DebugEventDispatcher@Events@Applications@Microsoft@@UEAA@XZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `??1DebugEventListener@Events@Applications@Microsoft@@UEAA@XZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `??1EventListenerService@telemetry_client@@UEAA@XZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `??1IAuthTokensController@Events@Applications@Microsoft@@UEAA@XZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `??1IHttpResponseCallback@telemetry_client@@UEAA@XZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `??1ILogManager@Events@Applications@Microsoft@@UEAA@XZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `??1ILogger@Events@Applications@Microsoft@@UEAA@XZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `??1IModule@Events@Applications@Microsoft@@UEAA@XZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `??1ISemanticContext@Events@Applications@Microsoft@@UEAA@XZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `??1OneDSWrapper@data_client@@UEAA@XZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `?ClearExperimentIds@ISemanticContext@Events@Applications@Microsoft@@UEAAXXZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `?Initialize@IModule@Events@Applications@Microsoft@@UEAAXPEAVILogManager@234@@Z` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 203 | `?SetCommonField@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@AEBUEventProperty@234@@Z` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 204 | `?SetCustomField@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@AEBUEventProperty@234@@Z` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `?SetEventExperimentIds@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@0@Z` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `?SetTicket@ISemanticContext@Events@Applications@Microsoft@@UEAAXW4TicketType@234@AEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `?Teardown@IModule@Events@Applications@Microsoft@@UEAAXXZ` | `0x137E60` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0EventListenerService@telemetry_client@@QEAA@AEBV01@@Z` | `0x138910` | 3,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0EventListenerService@telemetry_client@@QEAA@XZ` | `0x138910` | 3,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 271 | `FreeEventListenerService` | `0x139570` | 2,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `??0IHttpResponseCallback@telemetry_client@@QEAA@AEBV01@@Z` | `0x139E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??0IHttpResponseCallback@telemetry_client@@QEAA@XZ` | `0x139E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `??0OneDSWrapper@data_client@@QEAA@AEBV01@@Z` | `0x139E70` | 14,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `??0OneDSWrapper@data_client@@QEAA@XZ` | `0x139E70` | 14,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `FreeOneDSWrapper` | `0x13D7A0` | 12,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 270 | `FreeCommonSchemaHelper` | `0x140A30` | 120,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@EW4PiiKind@234@W4DataCategory@234@@Z` | `0x15E0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@CW4PiiKind@234@W4DataCategory@234@@Z` | `0x15E0F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 231 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@FW4PiiKind@234@W4DataCategory@234@@Z` | `0x15E100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@HW4PiiKind@234@W4DataCategory@234@@Z` | `0x15E110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@GW4PiiKind@234@W4DataCategory@234@@Z` | `0x15E120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@IW4PiiKind@234@W4DataCategory@234@@Z` | `0x15E130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@_KW4PiiKind@234@W4DataCategory@234@@Z` | `0x15E140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 194 | `?SetAppEnv@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x15E150` | 129 | UnwindData |  |
| 200 | `?SetAppName@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x15E230` | 129 | UnwindData |  |
| 196 | `?SetAppExperimentIds@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x15E310` | 129 | UnwindData |  |
| 197 | `?SetAppExperimentImpressionId@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x15E3F0` | 129 | UnwindData |  |
| 209 | `?SetDeviceOrgId@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x15E4D0` | 129 | UnwindData |  |
| 250 | `?SetUserMsaId@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x15E5B0` | 129 | UnwindData |  |
| 246 | `?SetUserANID@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x15E690` | 129 | UnwindData |  |
| 247 | `?SetUserAdvertisingId@ISemanticContext@Events@Applications@Microsoft@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x15E770` | 129 | UnwindData |  |
| 63 | `??0ISemanticContext@Events@Applications@Microsoft@@QEAA@AEBV0123@@Z` | `0x15E850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `??0ISemanticContext@Events@Applications@Microsoft@@QEAA@XZ` | `0x15E850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `??0ILogger@Events@Applications@Microsoft@@QEAA@AEBV0123@@Z` | `0x15E860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `??0ILogger@Events@Applications@Microsoft@@QEAA@XZ` | `0x15E860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `??0IModule@Events@Applications@Microsoft@@QEAA@AEBV0123@@Z` | `0x15E870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `??0IModule@Events@Applications@Microsoft@@QEAA@XZ` | `0x15E870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `??0ILogConfiguration@Events@Applications@Microsoft@@QEAA@XZ` | `0x15E880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `??0ILogConfiguration@Events@Applications@Microsoft@@QEAA@AEBV0123@@Z` | `0x15E8A0` | 64 | UnwindData |  |
| 50 | `??0ILogConfiguration@Events@Applications@Microsoft@@QEAA@$$QEAV0123@@Z` | `0x15E910` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `??4ILogConfiguration@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x15E990` | 43 | UnwindData |  |
| 122 | `??4ILogConfiguration@Events@Applications@Microsoft@@QEAAAEAV0123@$$QEAV0123@@Z` | `0x15E9C0` | 43 | UnwindData |  |
| 73 | `??0time_ticks_t@Events@Applications@Microsoft@@QEAA@XZ` | `0x1797B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??0time_ticks_t@Events@Applications@Microsoft@@QEAA@_K@Z` | `0x1797C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `??0time_ticks_t@Events@Applications@Microsoft@@QEAA@PEB_J@Z` | `0x1797D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `??0time_ticks_t@Events@Applications@Microsoft@@QEAA@$$QEAU0123@@Z` | `0x1797F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `??0time_ticks_t@Events@Applications@Microsoft@@QEAA@AEBU0123@@Z` | `0x1797F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `??4time_ticks_t@Events@Applications@Microsoft@@QEAAAEAU0123@$$QEAU0123@@Z` | `0x1797F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `??4time_ticks_t@Events@Applications@Microsoft@@QEAAAEAU0123@AEBU0123@@Z` | `0x1797F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??0GUID_t@Events@Applications@Microsoft@@QEAA@XZ` | `0x179800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `??0GUID_t@Events@Applications@Microsoft@@QEAA@PEBD@Z` | `0x179810` | 432 | UnwindData |  |
| 43 | `??0GUID_t@Events@Applications@Microsoft@@QEAA@QEBE_N@Z` | `0x1799C0` | 221 | UnwindData |  |
| 262 | `?to_bytes@GUID_t@Events@Applications@Microsoft@@QEBAXAEAY0BA@E@Z` | `0x179AA0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `??0GUID_t@Events@Applications@Microsoft@@QEAA@HHHAEBV?$initializer_list@E@std@@@Z` | `0x179AF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??0GUID_t@Events@Applications@Microsoft@@QEAA@$$QEAU0123@@Z` | `0x179B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `??0GUID_t@Events@Applications@Microsoft@@QEAA@AEBU0123@@Z` | `0x179B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `??4GUID_t@Events@Applications@Microsoft@@QEAAAEAU0123@$$QEAU0123@@Z` | `0x179B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `??4GUID_t@Events@Applications@Microsoft@@QEAAAEAU0123@AEBU0123@@Z` | `0x179B30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 255 | `?convertUintVectorToGUID@GUID_t@Events@Applications@Microsoft@@SA?AU_GUID@@AEBV?$vector@EV?$allocator@E@__Cr@std@@@__Cr@std@@@Z` | `0x179B50` | 121 | UnwindData |  |
| 264 | `?to_string@GUID_t@Events@Applications@Microsoft@@QEBA?AV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@XZ` | `0x179BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `?Hash@GUID_t@Events@Applications@Microsoft@@QEBA_KXZ` | `0x179BE0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `??8GUID_t@Events@Applications@Microsoft@@QEBA_NAEBU0123@@Z` | `0x179C40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `??MGUID_t@Events@Applications@Microsoft@@QEBA_NAEBU0123@@Z` | `0x179C70` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@$$QEAU0123@@Z` | `0x179CB0` | 67 | UnwindData |  |
| 137 | `??8EventProperty@Events@Applications@Microsoft@@QEBA_NAEBU0123@@Z` | `0x179D00` | 596 | UnwindData |  |
| 99 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@AEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x179FE0` | 104 | UnwindData |  |
| 112 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@PEBD@Z` | `0x17A050` | 86 | UnwindData |  |
| 265 | `?type_name@EventProperty@Events@Applications@Microsoft@@SAPEBDI@Z` | `0x17A0B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@_J@Z` | `0x17A120` | 38 | UnwindData |  |
| 116 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@_K@Z` | `0x17A120` | 38 | UnwindData |  |
| 108 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@H@Z` | `0x17A150` | 38 | UnwindData |  |
| 110 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@J@Z` | `0x17A150` | 38 | UnwindData |  |
| 104 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@C@Z` | `0x17A180` | 39 | UnwindData |  |
| 106 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@F@Z` | `0x17A1B0` | 39 | UnwindData |  |
| 105 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@E@Z` | `0x17A1E0` | 38 | UnwindData |  |
| 107 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@G@Z` | `0x17A210` | 38 | UnwindData |  |
| 109 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@I@Z` | `0x17A240` | 37 | UnwindData |  |
| 111 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@N@Z` | `0x17A270` | 47 | UnwindData |  |
| 117 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@_N@Z` | `0x17A2A0` | 36 | UnwindData |  |
| 114 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@Utime_ticks_t@123@@Z` | `0x17A2D0` | 41 | UnwindData |  |
| 113 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@UGUID_t@123@@Z` | `0x17A300` | 63 | UnwindData |  |
| 103 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@AEBV?$vector@_JV?$allocator@_J@__Cr@std@@@__Cr@std@@@Z` | `0x17A340` | 111 | UnwindData |  |
| 100 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@AEBV?$vector@NV?$allocator@N@__Cr@std@@@__Cr@std@@@Z` | `0x17A3E0` | 111 | UnwindData |  |
| 101 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@AEBV?$vector@UGUID_t@Events@Applications@Microsoft@@V?$allocator@UGUID_t@Events@Applications@Microsoft@@@__Cr@std@@@__Cr@std@@@Z` | `0x17A480` | 111 | UnwindData |  |
| 102 | `??4EventProperty@Events@Applications@Microsoft@@QEAAAEAU0123@AEBV?$vector@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@@__Cr@std@@@Z` | `0x17A520` | 125 | UnwindData |  |
| 34 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@Utime_ticks_t@123@W4PiiKind@123@W4DataCategory@123@@Z` | `0x17A5D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@UGUID_t@123@W4PiiKind@123@W4DataCategory@123@@Z` | `0x17A600` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@HW4PiiKind@123@W4DataCategory@123@@Z` | `0x17A640` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@JW4PiiKind@123@W4DataCategory@123@@Z` | `0x17A640` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@CW4PiiKind@123@W4DataCategory@123@@Z` | `0x17A670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@FW4PiiKind@123@W4DataCategory@123@@Z` | `0x17A6A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@EW4PiiKind@123@W4DataCategory@123@@Z` | `0x17A6D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@GW4PiiKind@123@W4DataCategory@123@@Z` | `0x17A700` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@IW4PiiKind@123@W4DataCategory@123@@Z` | `0x17A730` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@_KW4PiiKind@123@W4DataCategory@123@@Z` | `0x17A760` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@AEAV?$vector@_JV?$allocator@_J@__Cr@std@@@__Cr@std@@W4PiiKind@123@W4DataCategory@123@@Z` | `0x17A790` | 124 | UnwindData |  |
| 18 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@AEAV?$vector@NV?$allocator@N@__Cr@std@@@__Cr@std@@W4PiiKind@123@W4DataCategory@123@@Z` | `0x17A840` | 124 | UnwindData |  |
| 19 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@AEAV?$vector@UGUID_t@Events@Applications@Microsoft@@V?$allocator@UGUID_t@Events@Applications@Microsoft@@@__Cr@std@@@__Cr@std@@W4PiiKind@123@W4DataCategory@123@@Z` | `0x17A8F0` | 124 | UnwindData |  |
| 20 | `??0EventProperty@Events@Applications@Microsoft@@QEAA@AEAV?$vector@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@@__Cr@std@@W4PiiKind@123@W4DataCategory@123@@Z` | `0x17A9A0` | 138 | UnwindData |  |
| 4 | `??0DebugEventListener@Events@Applications@Microsoft@@QEAA@AEBV0123@@Z` | `0x17B6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0DebugEventListener@Events@Applications@Microsoft@@QEAA@XZ` | `0x17B6F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0DebugEventDispatcher@Events@Applications@Microsoft@@QEAA@AEBV0123@@Z` | `0x17B700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0DebugEventDispatcher@Events@Applications@Microsoft@@QEAA@XZ` | `0x17B700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0DebugEventSource@Events@Applications@Microsoft@@QEAA@AEBV0123@@Z` | `0x17B710` | 91 | UnwindData |  |
| 8 | `??0DebugEventSource@Events@Applications@Microsoft@@QEAA@XZ` | `0x17B7A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0DebugEventSource@Events@Applications@Microsoft@@QEAA@$$QEAV0123@@Z` | `0x17B7E0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `??4DebugEventSource@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x17B870` | 56 | UnwindData |  |
| 92 | `??4DebugEventSource@Events@Applications@Microsoft@@QEAAAEAV0123@$$QEAV0123@@Z` | `0x17B8B0` | 56 | UnwindData |  |
| 46 | `??0IAuthTokensController@Events@Applications@Microsoft@@QEAA@AEBV0123@@Z` | `0x17B8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `??0IAuthTokensController@Events@Applications@Microsoft@@QEAA@XZ` | `0x17B8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `??0LogConfiguration@Telemetry@Applications@Microsoft@@QEAA@AEBU0123@@Z` | `0x17B900` | 198 | UnwindData |  |
| 65 | `??0LogConfiguration@Telemetry@Applications@Microsoft@@QEAA@$$QEAU0123@@Z` | `0x17BA40` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `??4LogConfiguration@Telemetry@Applications@Microsoft@@QEAAAEAU0123@AEBU0123@@Z` | `0x17BAB0` | 83 | UnwindData |  |
| 130 | `??4LogConfiguration@Telemetry@Applications@Microsoft@@QEAAAEAU0123@$$QEAU0123@@Z` | `0x17BB10` | 83 | UnwindData |  |
| 88 | `??1LogConfiguration@Telemetry@Applications@Microsoft@@QEAA@XZ` | `0x17BB70` | 106 | UnwindData |  |
| 67 | `??0LogConfiguration@Telemetry@Applications@Microsoft@@QEAA@XZ` | `0x17BBE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `??0ILogController@Events@Applications@Microsoft@@QEAA@$$QEAV0123@@Z` | `0x17BC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `??0ILogController@Events@Applications@Microsoft@@QEAA@AEBV0123@@Z` | `0x17BC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??0ILogController@Events@Applications@Microsoft@@QEAA@XZ` | `0x17BC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `??0ILogManager@Events@Applications@Microsoft@@QEAA@AEBV0123@@Z` | `0x17BC20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??0ILogManager@Events@Applications@Microsoft@@QEAA@XZ` | `0x17BC20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `?GetDataInspector@ILogManager@Events@Applications@Microsoft@@UEAA?AV?$shared_ptr@VIDataInspector@Events@Applications@Microsoft@@@__Cr@std@@XZ` | `0x17BC50` | 88 | UnwindData |  |
| 13 | `??0EventProperties@Events@Applications@Microsoft@@QEAA@AEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@AEBV?$map@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UEventProperty@Events@Applications@Microsoft@@U?$less@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UEventProperty@Events@Applications@Microsoft@@@__Cr@std@@@23@@56@@Z` | `0x17BCB0` | 63 | UnwindData |  |
| 12 | `??0EventProperties@Events@Applications@Microsoft@@QEAA@AEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x17BD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `??YEventProperties@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV?$map@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UEventProperty@Events@Applications@Microsoft@@U?$less@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UEventProperty@Events@Applications@Microsoft@@@__Cr@std@@@23@@__Cr@std@@@Z` | `0x17BD50` | 347 | UnwindData |  |
| 96 | `??4EventProperties@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV?$map@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UEventProperty@Events@Applications@Microsoft@@U?$less@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UEventProperty@Events@Applications@Microsoft@@@__Cr@std@@@23@@__Cr@std@@@Z` | `0x17BF40` | 90 | UnwindData |  |
| 95 | `??4EventProperties@Events@Applications@Microsoft@@QEAAAEAV0123@AEBV0123@@Z` | `0x17BFC0` | 30 | UnwindData |  |
| 15 | `??0EventProperties@Events@Applications@Microsoft@@QEAA@AEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$initializer_list@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UEventProperty@Events@Applications@Microsoft@@@__Cr@std@@@6@@Z` | `0x17C070` | 69 | UnwindData |  |
| 97 | `??4EventProperties@Events@Applications@Microsoft@@QEAAAEAV0123@V?$initializer_list@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UEventProperty@Events@Applications@Microsoft@@@__Cr@std@@@std@@@Z` | `0x17C100` | 395 | UnwindData |  |
| 244 | `?SetTimestamp@EventProperties@Events@Applications@Microsoft@@QEAAX_J@Z` | `0x17C370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `?GetTimestamp@EventProperties@Events@Applications@Microsoft@@QEBA_JXZ` | `0x17C380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `?SetPriority@EventProperties@Events@Applications@Microsoft@@QEAAXW4EventPriority@234@@Z` | `0x17C390` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `?GetPriority@EventProperties@Events@Applications@Microsoft@@QEBA?AW4EventPriority@234@XZ` | `0x17C3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 211 | `?SetLatency@EventProperties@Events@Applications@Microsoft@@QEAAXW4EventLatency@234@@Z` | `0x17C3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `?SetPopsample@EventProperties@Events@Applications@Microsoft@@QEAAXN@Z` | `0x17C3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `?SetType@EventProperties@Events@Applications@Microsoft@@QEAA_NAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z` | `0x17C400` | 248 | UnwindData |  |
| 253 | `?TryGetLevel@EventProperties@Events@Applications@Microsoft@@QEBA?AV?$tuple@_NE@__Cr@std@@XZ` | `0x17C540` | 193 | UnwindData |  |
| 239 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@Utime_ticks_t@234@W4PiiKind@234@W4DataCategory@234@@Z` | `0x17C650` | 142 | UnwindData |  |
| 238 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@UGUID_t@234@W4PiiKind@234@W4DataCategory@234@@Z` | `0x17C6E0` | 142 | UnwindData |  |
| 228 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@AEAV?$vector@_JV?$allocator@_J@__Cr@std@@@67@W4PiiKind@234@W4DataCategory@234@@Z` | `0x17C770` | 114 | UnwindData |  |
| 225 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@AEAV?$vector@NV?$allocator@N@__Cr@std@@@67@W4PiiKind@234@W4DataCategory@234@@Z` | `0x17C7F0` | 114 | UnwindData |  |
| 226 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@AEAV?$vector@UGUID_t@Events@Applications@Microsoft@@V?$allocator@UGUID_t@Events@Applications@Microsoft@@@__Cr@std@@@67@W4PiiKind@234@W4DataCategory@234@@Z` | `0x17C870` | 114 | UnwindData |  |
| 227 | `?SetProperty@EventProperties@Events@Applications@Microsoft@@QEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@AEAV?$vector@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@@67@W4PiiKind@234@W4DataCategory@234@@Z` | `0x17C8F0` | 114 | UnwindData |  |
| 258 | `?erase@EventProperties@Events@Applications@Microsoft@@QEAA_KAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@W4DataCategory@234@@Z` | `0x17C970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `?GetPiiProperties@EventProperties@Events@Applications@Microsoft@@QEBA?BV?$map@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@U?$pair@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@W4PiiKind@Events@Applications@Microsoft@@@23@U?$less@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@U?$pair@V?$basic_string@DU?$char_traits@D@__Cr@std@@` | `0x17C990` | 544 | UnwindData |  |
| 260 | `?pack@EventProperties@Events@Applications@Microsoft@@QEAAPEAUevt_prop@@XZ` | `0x17CD00` | 533 | UnwindData |  |
| 266 | `?unpack@EventProperties@Events@Applications@Microsoft@@QEAA_NPEAUevt_prop@@_K@Z` | `0x17D0A0` | 979 | UnwindData |  |
| 193 | `?RemoveEventListener@DebugEventSource@Events@Applications@Microsoft@@UEAAXW4DebugEventType@234@AEAVDebugEventListener@234@@Z` | `0x180B10` | 205 | UnwindData |  |
| 167 | `?DetachEventSource@DebugEventSource@Events@Applications@Microsoft@@UEAA_NAEAV1234@@Z` | `0x180BE0` | 90 | UnwindData |  |
| 274 | `evt_api_call_default` | `0x1831B0` | 330 | UnwindData |  |
| 165 | `?CreateLogManager@LogManagerProvider@Events@Applications@Microsoft@@SAPEAVILogManager@234@PEBD_NAEAVILogConfiguration@234@AEAW4status_t@234@_K@Z` | `0x183300` | 155 | UnwindData |  |
| 164 | `?CreateLogManager@LogManagerProvider@Events@Applications@Microsoft@@SAPEAVILogManager@234@PEBDAEAW4status_t@234@_K@Z` | `0x1833A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `?CreateLogManager@LogManagerProvider@Events@Applications@Microsoft@@SAPEAVILogManager@234@AEAVILogConfiguration@234@AEAW4status_t@234@@Z` | `0x1833B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `?DestroyLogManager@LogManagerProvider@Events@Applications@Microsoft@@SA?AW4status_t@234@PEBD@Z` | `0x1833C0` | 8,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `?Get@LogManagerProvider@Events@Applications@Microsoft@@CAPEAVILogManager@234@PEBDAEAW4status_t@234@@Z` | `0x185330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 192 | `?Release@LogManagerProvider@Events@Applications@Microsoft@@SA?AW4status_t@234@PEBD@Z` | `0x185340` | 230,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 178 | `?GetModules@ILogConfiguration@Events@Applications@Microsoft@@QEAAAEAV?$map@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$shared_ptr@VIModule@Events@Applications@Microsoft@@@23@U?$less@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@V?$allocator@U?$pair@$$CBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$shared_ptr@VIModule@Events@Applications@Microsoft@@@23@@__Cr@std@@@23@@__Cr@std@@XZ` | `0x1BD720` | 5,296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `?DispatchEventBroadcast@ILogManager@Events@Applications@Microsoft@@SA_NVDebugEvent@234@@Z` | `0x1BEBD0` | 198 | UnwindData |  |
| 175 | `?GetDefaultConfiguration@Events@Applications@Microsoft@@YAAEBVILogConfiguration@123@XZ` | `0x1C0AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `?FromLogConfiguration@Events@Applications@Microsoft@@YA?AVILogConfiguration@123@AEAULogConfiguration@Telemetry@23@@Z` | `0x1C0AE0` | 1,457 | UnwindData |  |
| 170 | `?FromJSON@Events@Applications@Microsoft@@YA?AVILogConfiguration@123@PEBD@Z` | `0x1C1150` | 256 | UnwindData |  |
| 160 | `?AddModule@ILogConfiguration@Events@Applications@Microsoft@@QEAAXPEBDAEBV?$shared_ptr@VIModule@Events@Applications@Microsoft@@@__Cr@std@@@Z` | `0x1C22D0` | 146 | UnwindData |  |
| 275 | `sqlite3_dbdata_init` | `0x1C5650` | 88 | UnwindData |  |
| 146 | `??_7EventListenerService@telemetry_client@@6B@` | `0x242170` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `??_7OneDSWrapper@data_client@@6B@` | `0x2422B0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `??_7DebugEventSource@Events@Applications@Microsoft@@6B@` | `0x242540` | 168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `??_7IHttpResponseCallback@telemetry_client@@6B@` | `0x2425E8` | 5,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `??_7ISemanticContext@Events@Applications@Microsoft@@6B@` | `0x243988` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `??_7ILogger@Events@Applications@Microsoft@@6B@` | `0x243A98` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `??_7IModule@Events@Applications@Microsoft@@6B@` | `0x243BC8` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `??_7EventProperty@Events@Applications@Microsoft@@6B@` | `0x243C78` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `??_7DebugEventListener@Events@Applications@Microsoft@@6B@` | `0x243C98` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `??_7DebugEventDispatcher@Events@Applications@Microsoft@@6B@` | `0x243CB8` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `??_7IAuthTokensController@Events@Applications@Microsoft@@6B@` | `0x243CD8` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `??_7ILogController@Events@Applications@Microsoft@@6B@` | `0x243D28` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `??_7ILogManager@Events@Applications@Microsoft@@6BILogController@123@@` | `0x243D98` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `??_7ILogManager@Events@Applications@Microsoft@@6BIContextProvider@123@@` | `0x243F48` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `??_7ILogManager@Events@Applications@Microsoft@@6BDebugEventDispatcher@123@@` | `0x243F68` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `??_7EventProperties@Events@Applications@Microsoft@@6B@` | `0x243F80` | 835,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 259 | `?lock@?1??stateLock@DebugEventSource@Events@Applications@Microsoft@@KAAEAVrecursive_mutex@__Cr@std@@XZ@4V?$Leaky@Vrecursive_mutex@__Cr@std@@@345@A` | `0x30FE90` | 40 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `?$TSS0@?1??stateLock@DebugEventSource@Events@Applications@Microsoft@@KAAEAVrecursive_mutex@__Cr@std@@XZ@4HA` | `0x30FEB8` | 0 | Indeterminate |  |
