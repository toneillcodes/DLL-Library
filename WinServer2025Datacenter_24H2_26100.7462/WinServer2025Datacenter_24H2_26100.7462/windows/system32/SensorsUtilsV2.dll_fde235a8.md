# Binary Specification: SensorsUtilsV2.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SensorsUtilsV2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fde235a8619a871bcaa0a731c8b953eb613f88ce37407dfc6f4fad640bd8fbe0`
* **Total Exported Functions:** 71

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 35 | `GetSetting` | `0xA380` | 4,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AddMillisecondsToFileTime` | `0xB4D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CollectionsListAllocateBufferAndSerialize` | `0xB510` | 399 | UnwindData |  |
| 3 | `CollectionsListCopyAndMarshall` | `0xB6B0` | 419 | UnwindData |  |
| 4 | `CollectionsListDeserializeFromBuffer` | `0xB860` | 1,324 | UnwindData |  |
| 5 | `CollectionsListGetFillableCount` | `0xBDA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `CollectionsListGetMarshalledSize` | `0xBDD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `CollectionsListGetMarshalledSizeWithoutSerialization` | `0xBDF0` | 131 | UnwindData |  |
| 8 | `CollectionsListGetSerializedSize` | `0xBE80` | 500 | UnwindData |  |
| 9 | `CollectionsListMarshall` | `0xC080` | 390 | UnwindData |  |
| 10 | `CollectionsListSerializeToBuffer` | `0xC210` | 881 | UnwindData |  |
| 11 | `CollectionsListSortSubscribedActivitiesByConfidence` | `0xC590` | 1,175 | UnwindData |  |
| 12 | `CollectionsListUpdateMarshalledPointer` | `0xCA30` | 268 | UnwindData |  |
| 13 | `ConvertAccelerometerDataToCollection` | `0xCB50` | 206 | UnwindData |  |
| 14 | `ConvertCollectionToAccelerometerData` | `0xCC30` | 200 | UnwindData |  |
| 15 | `ConvertCollectionToGyroscopeData` | `0xCE60` | 98 | UnwindData |  |
| 16 | `ConvertCollectionToLightSensorData` | `0xCED0` | 27 | UnwindData |  |
| 17 | `ConvertCollectionToLightSensorDataWithColor` | `0xCF00` | 645 | UnwindData |  |
| 18 | `ConvertCollectionToMagnetometerData` | `0xD190` | 168 | UnwindData |  |
| 19 | `ConvertCollectionToOrientationData` | `0xD240` | 827 | UnwindData |  |
| 20 | `ConvertCollectionToProximitySensorData` | `0xD590` | 201 | UnwindData |  |
| 21 | `ConvertFloat3DDataToCollection` | `0xD660` | 207 | UnwindData |  |
| 22 | `ConvertGyroscopeDataToCollection` | `0xD740` | 99 | UnwindData |  |
| 23 | `ConvertLightSensorDataToCollection` | `0xD7B0` | 115 | UnwindData |  |
| 24 | `ConvertLightSensorDataWithColorToCollection` | `0xD830` | 357 | UnwindData |  |
| 25 | `ConvertMagnetometerDataToCollection` | `0xD9A0` | 200 | UnwindData |  |
| 26 | `ConvertOrientationDataToCollection` | `0xDA70` | 708 | UnwindData |  |
| 27 | `ConvertProximitySensorDataToCollection` | `0xDD40` | 170 | UnwindData |  |
| 28 | `ConvertSimpleOrientationDataToCollection` | `0xDDF0` | 115 | UnwindData |  |
| 29 | `EvaluateActivityThresholds` | `0xDE70` | 1,157 | UnwindData |  |
| 30 | `GetBiosInformation` | `0xE300` | 204 | UnwindData |  |
| 31 | `GetDeviceClassStr` | `0xE3E0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `GetFileTimeDifference` | `0xE430` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `GetFileTimeFromTimeStamp` | `0xE480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `GetTimeStampFromFileTime` | `0xE480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `GetPerformanceTime` | `0xE4A0` | 243 | UnwindData |  |
| 36 | `GetSystemTableInfo` | `0xE5A0` | 285 | UnwindData |  |
| 38 | `InitPropVariantFromCLSIDArray` | `0xE6D0` | 141 | UnwindData |  |
| 39 | `InitPropVariantFromFloat` | `0xE770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `InitPropVariantFromFloatVector` | `0xE790` | 158 | UnwindData |  |
| 41 | `IsCollectionListSame` | `0xE9E0` | 317 | UnwindData |  |
| 42 | `IsGUIDPresentInList` | `0xEB30` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `IsKeyPresentInCollectionList` | `0xEB70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `IsKeyPresentInPropertyList` | `0xEBD0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `IsSensorSubscribed` | `0xEC70` | 125 | UnwindData |  |
| 46 | `IsTestSigningOn` | `0xED00` | 115 | UnwindData |  |
| 47 | `MapActivityConfidenceToState` | `0xEE10` | 353 | UnwindData |  |
| 48 | `PropKeyFindKeyGetBool` | `0xEF80` | 137 | UnwindData |  |
| 49 | `PropKeyFindKeyGetDouble` | `0xF010` | 137 | UnwindData |  |
| 50 | `PropKeyFindKeyGetFileTime` | `0xF0A0` | 124 | UnwindData |  |
| 51 | `PropKeyFindKeyGetFloat` | `0xF130` | 113 | UnwindData |  |
| 52 | `PropKeyFindKeyGetGuid` | `0xF1B0` | 137 | UnwindData |  |
| 53 | `PropKeyFindKeyGetInt32` | `0xF240` | 137 | UnwindData |  |
| 54 | `PropKeyFindKeyGetInt64` | `0xF2D0` | 137 | UnwindData |  |
| 55 | `PropKeyFindKeyGetNthInt64` | `0xF360` | 177 | UnwindData |  |
| 56 | `PropKeyFindKeyGetNthUlong` | `0xF420` | 177 | UnwindData |  |
| 57 | `PropKeyFindKeyGetNthUshort` | `0xF4E0` | 177 | UnwindData |  |
| 58 | `PropKeyFindKeyGetPropVariant` | `0xF5A0` | 195 | UnwindData |  |
| 59 | `PropKeyFindKeyGetUlong` | `0xF670` | 137 | UnwindData |  |
| 60 | `PropKeyFindKeyGetUshort` | `0xF700` | 137 | UnwindData |  |
| 61 | `PropKeyFindKeySetPropVariant` | `0xF790` | 195 | UnwindData |  |
| 62 | `PropVariantGetInformation` | `0xF860` | 327 | UnwindData |  |
| 63 | `PropVariantToFloatVector` | `0xF9B0` | 84 | UnwindData |  |
| 64 | `PropertiesListCopy` | `0xFA10` | 187 | UnwindData |  |
| 65 | `PropertiesListGetFillableCount` | `0xFAE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `SensorCollectionGetAt` | `0xFB10` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `SensorsQueryDeviceCompatFlags` | `0xFB90` | 186 | UnwindData |  |
| 68 | `SensorsQueryDeviceCompatFlagsUsingSmbiosInformation` | `0xFC50` | 443 | UnwindData |  |
| 69 | `SensorsQueryDeviceCompatFlagsUsingSystemInformation` | `0xFE20` | 418 | UnwindData |  |
| 70 | `SerializationBufferAllocate` | `0xFFD0` | 99 | UnwindData |  |
| 71 | `SerializationBufferFree` | `0x10040` | 27 | UnwindData |  |
