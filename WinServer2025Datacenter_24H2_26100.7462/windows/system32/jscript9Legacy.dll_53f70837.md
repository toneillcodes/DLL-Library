# Binary Specification: jscript9Legacy.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\jscript9Legacy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `53f70837d151d1732c9d3f43bf776ac2e13fb643ffb94683433646616bffcc62`
* **Total Exported Functions:** 97

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x41AC0` | 226 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x41BB0` | 904 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x420A0` | 113 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x42120` | 111 | UnwindData |  |
| 5 | `JsAddRef` | `0x60A40` | 46 | UnwindData |  |
| 6 | `JsBoolToBoolean` | `0x60A80` | 46 | UnwindData |  |
| 7 | `JsBooleanToBool` | `0x60AC0` | 46 | UnwindData |  |
| 8 | `JsCallFunction` | `0x60B00` | 71 | UnwindData |  |
| 9 | `JsCollectGarbage` | `0x60B50` | 25 | UnwindData |  |
| 10 | `JsConstructObject` | `0x60B70` | 71 | UnwindData |  |
| 11 | `JsConvertValueToBoolean` | `0x60BC0` | 46 | UnwindData |  |
| 12 | `JsConvertValueToNumber` | `0x60C00` | 46 | UnwindData |  |
| 13 | `JsConvertValueToObject` | `0x60C40` | 46 | UnwindData |  |
| 14 | `JsConvertValueToString` | `0x60C80` | 46 | UnwindData |  |
| 15 | `JsCreateArray` | `0x60CC0` | 46 | UnwindData |  |
| 16 | `JsCreateContext` | `0x60D00` | 58 | UnwindData |  |
| 17 | `JsCreateError` | `0x60D40` | 46 | UnwindData |  |
| 18 | `JsCreateExternalObject` | `0x60D80` | 58 | UnwindData |  |
| 19 | `JsCreateExternalType` | `0x60DC0` | 46 | UnwindData |  |
| 20 | `JsCreateFunction` | `0x60E00` | 58 | UnwindData |  |
| 21 | `JsCreateObject` | `0x60E40` | 25 | UnwindData |  |
| 22 | `JsCreateRangeError` | `0x60E60` | 46 | UnwindData |  |
| 23 | `JsCreateReferenceError` | `0x60EA0` | 46 | UnwindData |  |
| 24 | `JsCreateRuntime` | `0x60EE0` | 70 | UnwindData |  |
| 25 | `JsCreateSyntaxError` | `0x60F30` | 46 | UnwindData |  |
| 26 | `JsCreateTypeError` | `0x60F70` | 46 | UnwindData |  |
| 27 | `JsCreateTypedExternalObject` | `0x60FB0` | 58 | UnwindData |  |
| 28 | `JsCreateURIError` | `0x60FF0` | 46 | UnwindData |  |
| 29 | `JsDefineProperty` | `0x61030` | 70 | UnwindData |  |
| 30 | `JsDeleteIndexedProperty` | `0x61080` | 46 | UnwindData |  |
| 31 | `JsDeleteProperty` | `0x610C0` | 70 | UnwindData |  |
| 32 | `JsDisableRuntimeExecution` | `0x61110` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `JsDisposeRuntime` | `0x61170` | 25 | UnwindData |  |
| 34 | `JsDoubleToNumber` | `0x61190` | 48 | UnwindData |  |
| 35 | `JsEnableRuntimeExecution` | `0x611D0` | 25 | UnwindData |  |
| 36 | `JsEnumerateHeap` | `0x611F0` | 112 | UnwindData |  |
| 37 | `JsEquals` | `0x61270` | 58 | UnwindData |  |
| 38 | `JsGetAndClearException` | `0x612B0` | 192 | UnwindData |  |
| 39 | `JsGetCurrentContext` | `0x61380` | 57 | UnwindData |  |
| 40 | `JsGetDefaultTypeDescription` | `0x613C0` | 25 | UnwindData |  |
| 41 | `JsGetExtensionAllowed` | `0x613E0` | 46 | UnwindData |  |
| 42 | `JsGetExternalData` | `0x61420` | 46 | UnwindData |  |
| 43 | `JsGetExternalType` | `0x61460` | 46 | UnwindData |  |
| 44 | `JsGetFalseValue` | `0x614A0` | 25 | UnwindData |  |
| 45 | `JsGetGlobalObject` | `0x614C0` | 25 | UnwindData |  |
| 46 | `JsGetIndexedProperty` | `0x614E0` | 58 | UnwindData |  |
| 47 | `JsGetNullValue` | `0x61520` | 25 | UnwindData |  |
| 48 | `JsGetOwnPropertyDescriptor` | `0x61540` | 58 | UnwindData |  |
| 49 | `JsGetOwnPropertyNames` | `0x61580` | 46 | UnwindData |  |
| 50 | `JsGetProperty` | `0x615C0` | 58 | UnwindData |  |
| 51 | `JsGetPropertyIdFromName` | `0x61600` | 46 | UnwindData |  |
| 52 | `JsGetPropertyNameFromId` | `0x61640` | 46 | UnwindData |  |
| 53 | `JsGetPrototype` | `0x61680` | 46 | UnwindData |  |
| 54 | `JsGetRuntime` | `0x616C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `JsGetRuntimeMemoryLimit` | `0x61710` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `JsGetRuntimeMemoryUsage` | `0x61750` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `JsGetStringLength` | `0x61790` | 46 | UnwindData |  |
| 58 | `JsGetTrueValue` | `0x617D0` | 25 | UnwindData |  |
| 59 | `JsGetUndefinedValue` | `0x617F0` | 25 | UnwindData |  |
| 60 | `JsGetValueType` | `0x61810` | 46 | UnwindData |  |
| 61 | `JsHasException` | `0x61850` | 165 | UnwindData |  |
| 62 | `JsHasExternalData` | `0x61900` | 46 | UnwindData |  |
| 63 | `JsHasIndexedProperty` | `0x61940` | 58 | UnwindData |  |
| 64 | `JsHasProperty` | `0x61980` | 58 | UnwindData |  |
| 65 | `JsIdle` | `0x619C0` | 25 | UnwindData |  |
| 66 | `JsIntToNumber` | `0x619E0` | 46 | UnwindData |  |
| 67 | `JsIsEnumeratingHeap` | `0x61A20` | 89 | UnwindData |  |
| 68 | `JsIsRuntimeExecutionDisabled` | `0x61A80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `JsNumberToDouble` | `0x61AC0` | 46 | UnwindData |  |
| 70 | `JsParseScript` | `0x61B00` | 44 | UnwindData |  |
| 71 | `JsParseSerializedScript` | `0x61B40` | 48 | UnwindData |  |
| 72 | `JsPointerToString` | `0x61B80` | 58 | UnwindData |  |
| 73 | `JsPreventExtension` | `0x61BC0` | 25 | UnwindData |  |
| 74 | `JsRelease` | `0x61BE0` | 46 | UnwindData |  |
| 75 | `JsRunScript` | `0x61C20` | 44 | UnwindData |  |
| 76 | `JsRunSerializedScript` | `0x61C60` | 48 | UnwindData |  |
| 77 | `JsSerializeScript` | `0x61CA0` | 203 | UnwindData |  |
| 78 | `JsSetCurrentContext` | `0x61D80` | 25 | UnwindData |  |
| 79 | `JsSetException` | `0x61DA0` | 25 | UnwindData |  |
| 80 | `JsSetExternalData` | `0x61DC0` | 46 | UnwindData |  |
| 81 | `JsSetIndexedProperty` | `0x61E00` | 58 | UnwindData |  |
| 82 | `JsSetProperty` | `0x61E40` | 70 | UnwindData |  |
| 83 | `JsSetPrototype` | `0x61E90` | 46 | UnwindData |  |
| 84 | `JsSetRuntimeBeforeCollectCallback` | `0x61ED0` | 58 | UnwindData |  |
| 85 | `JsSetRuntimeMemoryAllocationCallback` | `0x61F10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `JsSetRuntimeMemoryLimit` | `0x61F50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `JsStartDebugging` | `0x61F80` | 25 | UnwindData |  |
| 88 | `JsStartProfiling` | `0x61FA0` | 58 | UnwindData |  |
| 89 | `JsStopProfiling` | `0x61FE0` | 24 | UnwindData |  |
| 90 | `JsStrictEquals` | `0x62000` | 58 | UnwindData |  |
| 91 | `JsStringToPointer` | `0x62040` | 58 | UnwindData |  |
| 92 | `JsValueToVariant` | `0x62080` | 46 | UnwindData |  |
| 97 | `JsVariantToValue` | `0x620C0` | 46 | UnwindData |  |
| 93 | `JsVarAddRef` | `0x82EB0` | 100 | UnwindData |  |
| 94 | `JsVarRelease` | `0x82F20` | 80 | UnwindData |  |
| 95 | `JsVarToExtension` | `0x82F80` | 117 | UnwindData |  |
| 96 | `JsVarToScriptDirect` | `0x83000` | 94 | UnwindData |  |
