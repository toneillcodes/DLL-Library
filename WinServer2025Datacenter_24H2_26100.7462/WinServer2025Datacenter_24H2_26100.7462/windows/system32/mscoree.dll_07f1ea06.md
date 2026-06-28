# Binary Specification: mscoree.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mscoree.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `07f1ea065c452d37da2ad56ce505184e41947c42a560d8235276e0fb8b758701`
* **Total Exported Functions:** 125

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 72 | `GetCORVersion` | `0x1010` | 299 | UnwindData |  |
| 82 | `GetMetaDataInternalInterface` | `0x1150` | 357 | UnwindData |  |
| 54 | `CorGetSvc` | `0x12C0` | 259 | UnwindData |  |
| 38 | `CLRCreateInstance` | `0x13D0` | 196 | UnwindData |  |
| 105 | `ND_RU1` | `0x14A0` | 321 | UnwindData |  |
| 62 | `DllGetClassObject` | `0x15F0` | 338 | UnwindData |  |
| 58 | `CreateConfigStream` | `0x1750` | 306 | UnwindData |  |
| 31 | `GetTargetForVTableEntry` | `0x1890` | 64 | UnwindData |  |
| 103 | `ND_RI4` | `0x1A00` | 276 | UnwindData |  |
| 37 | `SetTargetForVTableEntry` | `0x1B20` | 72 | UnwindData |  |
| 104 | `ND_RI8` | `0x1CB0` | 279 | UnwindData |  |
| 32 | `GetTokenForVTableEntry` | `0x1DD0` | 49 | UnwindData |  |
| 136 | `_CorDllMain` | `0x1FD0` | 72 | UnwindData |  |
| 71 | `GetCORSystemDirectory` | `0x6BD0` | 298 | UnwindData |  |
| 53 | `CorExitProcess` | `0x6D00` | 262 | UnwindData |  |
| 29 | `GetProcessExecutableHeap` | `0x6F00` | 255 | UnwindData |  |
| 51 | `CorBindToRuntimeEx` | `0x70E0` | 455 | UnwindData |  |
| 70 | `GetCORRootDirectory` | `0x72B0` | 309 | UnwindData |  |
| 87 | `GetRequestedRuntimeInfo` | `0x73F0` | 596 | UnwindData |  |
| 109 | `ND_WU1` | `0x7650` | 309 | UnwindData |  |
| 24 | *Ordinal Only* | `0x7790` | 172 | UnwindData |  |
| 137 | `_CorExeMain` | `0x7850` | 59 | UnwindData |  |
| 25 | `CollectCtrs` | `0x7BC0` | 327 | UnwindData |  |
| 36 | `OpenCtrs` | `0x7D10` | 259 | UnwindData |  |
| 102 | `ND_RI2` | `0x7E50` | 270 | UnwindData |  |
| 98 | `LockClrVersion` | `0x7F70` | 32 | UnwindData |  |
| 61 | `DllCanUnloadNow` | `0x8100` | 244 | UnwindData |  |
| 81 | `GetHostConfigurationFile` | `0x8200` | 281 | UnwindData |  |
| 107 | `ND_WI4` | `0x8320` | 283 | UnwindData |  |
| 43 | `CoInitializeEE` | `0x8450` | 255 | UnwindData |  |
| 94 | `IEE` | `0x8570` | 241 | UnwindData |  |
| 142 | *Ordinal Only* | `0x8670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `CorBindToRuntime` | `0x8690` | 395 | UnwindData |  |
| 108 | `ND_WI8` | `0x8880` | 284 | UnwindData |  |
| 52 | `CorBindToRuntimeHost` | `0x9000` | 488 | UnwindData |  |
| 18 | `PostError` | `0x20390` | 37 | UnwindData |  |
| 21 | `CloseCtrs` | `0x203C0` | 255 | UnwindData |  |
| 26 | `CorDllMainWorker` | `0x204D0` | 264 | UnwindData |  |
| 27 | `EEDllGetClassObjectFromClass` | `0x206E0` | 285 | UnwindData |  |
| 28 | `GetPrivateContextsPerfCounters` | `0x20810` | 296 | UnwindData |  |
| 30 | `GetStartupFlags` | `0x20940` | 216 | UnwindData |  |
| 17 | `InitErrors` | `0x20A20` | 305 | UnwindData |  |
| 19 | `InitSSAutoEnterThread` | `0x20B60` | 292 | UnwindData |  |
| 33 | `LogHelp_LogAssert` | `0x20C90` | 329 | UnwindData |  |
| 34 | `LogHelp_NoGuiOnAssert` | `0x20DE0` | 294 | UnwindData |  |
| 35 | `LogHelp_TerminateOnAssert` | `0x20F10` | 286 | UnwindData |  |
| 20 | `UpdateError` | `0x21040` | 284 | UnwindData |  |
| 39 | `CallFunctionShim` | `0x21170` | 413 | UnwindData |  |
| 40 | `ClrCreateManagedInstance` | `0x21320` | 271 | UnwindData |  |
| 41 | `CoEEShutDownCOM` | `0x21440` | 286 | UnwindData |  |
| 42 | `CoInitializeCor` | `0x21570` | 294 | UnwindData |  |
| 44 | `CoUninitializeCor` | `0x216A0` | 286 | UnwindData |  |
| 45 | `CoUninitializeEE` | `0x217D0` | 296 | UnwindData |  |
| 46 | `CorBindToCurrentRuntime` | `0x21900` | 297 | UnwindData |  |
| 48 | `CorBindToRuntimeByCfg` | `0x21A30` | 369 | UnwindData |  |
| 49 | `CorBindToRuntimeByPath` | `0x21BB0` | 250 | UnwindData |  |
| 50 | `CorBindToRuntimeByPathEx` | `0x21CB0` | 271 | UnwindData |  |
| 55 | `CorIsLatestSvc` | `0x21DD0` | 250 | UnwindData |  |
| 56 | `CorMarkThreadInThreadPool` | `0x21ED0` | 194 | UnwindData |  |
| 57 | `CorTickleSvc` | `0x21FA0` | 217 | UnwindData |  |
| 59 | `CreateDebuggingInterfaceFromVersion` | `0x22080` | 267 | UnwindData |  |
| 63 | `DllRegisterServer` | `0x221A0` | 217 | UnwindData |  |
| 64 | `DllUnregisterServer` | `0x22280` | 217 | UnwindData |  |
| 65 | `EEDllRegisterServer` | `0x22360` | 297 | UnwindData |  |
| 66 | `EEDllUnregisterServer` | `0x22490` | 297 | UnwindData |  |
| 67 | `GetAssemblyMDImport` | `0x225C0` | 271 | UnwindData |  |
| 69 | `GetCORRequiredVersion` | `0x226E0` | 267 | UnwindData |  |
| 73 | `GetCompileInfo` | `0x22800` | 296 | UnwindData |  |
| 74 | `GetFileVersion` | `0x22930` | 297 | UnwindData |  |
| 75 | `GetHashFromAssemblyFile` | `0x22A60` | 336 | UnwindData |  |
| 76 | `GetHashFromAssemblyFileW` | `0x22BC0` | 336 | UnwindData |  |
| 77 | `GetHashFromBlob` | `0x22D20` | 365 | UnwindData |  |
| 78 | `GetHashFromFile` | `0x22EA0` | 336 | UnwindData |  |
| 79 | `GetHashFromFileW` | `0x23000` | 336 | UnwindData |  |
| 80 | `GetHashFromHandle` | `0x23160` | 336 | UnwindData |  |
| 83 | `GetMetaDataInternalInterfaceFromPublic` | `0x232C0` | 271 | UnwindData |  |
| 84 | `GetMetaDataPublicInterfaceFromInternal` | `0x233E0` | 271 | UnwindData |  |
| 85 | `GetPermissionRequests` | `0x23500` | 415 | UnwindData |  |
| 86 | `GetRealProcAddress` | `0x236B0` | 322 | UnwindData |  |
| 88 | `GetRequestedRuntimeVersion` | `0x23800` | 297 | UnwindData |  |
| 89 | `GetRequestedRuntimeVersionForCLSID` | `0x23930` | 330 | UnwindData |  |
| 90 | `GetVersionFromProcess` | `0x23A80` | 297 | UnwindData |  |
| 91 | `GetXMLElement` | `0x23BB0` | 244 | UnwindData |  |
| 92 | `GetXMLElementAttribute` | `0x23CB0` | 285 | UnwindData |  |
| 93 | `GetXMLObject` | `0x23DE0` | 235 | UnwindData |  |
| 95 | `LoadLibraryShim` | `0x23EE0` | 294 | UnwindData |  |
| 96 | `LoadLibraryWithPolicyShim` | `0x24010` | 297 | UnwindData |  |
| 22 | `LoadStringRC` | `0x24140` | 293 | UnwindData |  |
| 97 | `LoadStringRCEx` | `0x24270` | 361 | UnwindData |  |
| 99 | `MetaDataGetDispenser` | `0x243E0` | 271 | UnwindData |  |
| 100 | `ND_CopyObjDst` | `0x24500` | 288 | UnwindData |  |
| 101 | `ND_CopyObjSrc` | `0x24630` | 286 | UnwindData |  |
| 106 | `ND_WI2` | `0x24760` | 255 | UnwindData |  |
| 23 | `ReOpenMetaDataWithMemory` | `0x24970` | 271 | UnwindData |  |
| 110 | `ReOpenMetaDataWithMemoryEx` | `0x24A90` | 297 | UnwindData |  |
| 111 | `RunDll32ShimW` | `0x24BC0` | 297 | UnwindData |  |
| 112 | `RuntimeOSHandle` | `0x24CF0` | 312 | UnwindData |  |
| 113 | `RuntimeOpenImage` | `0x24E30` | 312 | UnwindData |  |
| 114 | `RuntimeReleaseHandle` | `0x24F70` | 297 | UnwindData |  |
| 115 | `StrongNameCompareAssemblies` | `0x250A0` | 268 | UnwindData |  |
| 116 | `StrongNameErrorInfo` | `0x251C0` | 297 | UnwindData |  |
| 117 | `StrongNameFreeBuffer` | `0x252F0` | 298 | UnwindData |  |
| 118 | `StrongNameGetBlob` | `0x25420` | 268 | UnwindData |  |
| 119 | `StrongNameGetBlobFromImage` | `0x25540` | 290 | UnwindData |  |
| 120 | `StrongNameGetPublicKey` | `0x25670` | 333 | UnwindData |  |
| 121 | `StrongNameHashSize` | `0x257D0` | 325 | UnwindData |  |
| 122 | `StrongNameKeyDelete` | `0x25920` | 308 | UnwindData |  |
| 123 | `StrongNameKeyGen` | `0x25A60` | 290 | UnwindData |  |
| 124 | `StrongNameKeyGenEx` | `0x25B90` | 329 | UnwindData |  |
| 125 | `StrongNameKeyInstall` | `0x25CE0` | 268 | UnwindData |  |
| 126 | `StrongNameSignatureGeneration` | `0x25E00` | 372 | UnwindData |  |
| 127 | `StrongNameSignatureGenerationEx` | `0x25F80` | 406 | UnwindData |  |
| 128 | `StrongNameSignatureSize` | `0x26120` | 346 | UnwindData |  |
| 129 | `StrongNameSignatureVerification` | `0x26280` | 346 | UnwindData |  |
| 130 | `StrongNameSignatureVerificationEx` | `0x263E0` | 268 | UnwindData |  |
| 131 | `StrongNameSignatureVerificationFromImage` | `0x26500` | 290 | UnwindData |  |
| 132 | `StrongNameTokenFromAssembly` | `0x26630` | 268 | UnwindData |  |
| 133 | `StrongNameTokenFromAssemblyEx` | `0x26750` | 333 | UnwindData |  |
| 134 | `StrongNameTokenFromPublicKey` | `0x268B0` | 355 | UnwindData |  |
| 135 | `TranslateSecurityAttributes` | `0x26A20` | 375 | UnwindData |  |
| 138 | `_CorExeMain2` | `0x26D40` | 49 | UnwindData |  |
| 60 | `CreateInterface` | `0x26D80` | 153 | UnwindData |  |
| 68 | `GetCLRMetaHost` | `0x26E20` | 138 | UnwindData |  |
| 139 | `_CorImageUnloading` | `0x2F750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `_CorValidateImage` | `0x2F760` | 490 | UnwindData |  |
