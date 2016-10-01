#!/usr/bin/python2
# -*- coding: utf-8 -*-

TAG_LIST = {
  #exif
  "exiftags" : {
    "0001" : {
      "tag" : "Interpindex",
      "description" : "???"
    },
    "0002" : {
      "tag" : "InteropVersion",
      "description" : "???"
    },
    "000B" : {
      "tag" : "ProcessingSoftware",
      "description" : "???"
    },
    "00fe" : {
      "tag" : "Subfile Type",
      "description" : "???"
    },
    "00ff" : {
      "tag" : "OldSubfile Type",
      "description" : "???"
    },
    "0100" : {
      "tag" : "ImageWidth",
      "description" : "画像の幅"
    },
    "0101" : {
      "tag" : "ImageLength",
      "description" : "画像の高さ"
    },
    "0102" : {
      "tag" : "BitsPerSample",
      "description" : "画像のビットの深さ"
    },
    "0103" : {
      "tag" : "Compression",
      "description" : "圧縮の種類",
      "mean" : {
        "1" : "非圧縮",
        "6" : "JPEG圧縮(サムネイルのみ)",
      }
    },
    "0106" : {
      "tag" : "PhotometricInterpretation",
      "description" : "画素構成",
      "mean" : {
        "2" : "RGB",
        "6" : "YCbCr",
      }
    },
    "0107" : {
      "tag" : "Thresholding",
      "description" : "???"
    },
    "0108" : {
      "tag" : "CellWidth",
      "description" : "???"
    },
    "0109" : {
      "tag" : "CellLength",
      "description" : "???"
    },
    "010a" : {
      "tag" : "FillOrder",
      "description" : "???"
    },
    "010d" : {
      "tag" : "DocumentName",
      "description" : "???"
    },
    "010e" : {
      "tag" : "ImageDescription",
      "description" : "画像タイトル"
    },
    "010f" : {
      "tag" : "Make",
      "description" : "画像入力機器のメーカー名"
    },
    "0110" : {
      "tag" : "Model",
      "description" : "画像入力機器のモデル名"
    },
    "0111" : {
      "tag" : "StripOffsets",
      "description" : "画像データのロケーション,"
    },
    "0112" : {
      "tag" : "Orientation",
      "description" : "画像方向",
      "mean" : {
        "1" : "visual topvisual left-hand side",
        "2" : "visual topvisual right-hand side",
        "3" : "visual bottomvisual right-hand side",
        "4" : "visual bottomvisual left-hand side",
        "5" : "visual left-hand sidevisual top",
        "6" : "visual right-hand sidevisual top",
        "7" : "visual right-hand sidevisual bottom",
        "8" : "visual left-hand sidevisual bottom",
      }
    },
    "0115" : {
      "tag" : "SamplesPerPixel",
      "description" : "コンポーネント数"
    },
    "0116" : {
      "tag" : "RowsPerStrip",
      "description" : "1ストリップあたりの行の数"
    },
    "0117" : {
      "tag" : "StripByteCounts",
      "description" : "ストリップの総バイト数"
    },
    "0118" : {
      "tag" : "MinSampleValue",
      "description" : "???"
    },
    "0119" : {
      "tag" : "MaxSampleValue",
      "description" : "???"
    },
    "011a" : {
      "tag" : "XResolution",
      "description" : "画像の幅の解像度"
    },
    "011b" : {
      "tag" : "YResolution",
      "description" : "画像の高さの解像度"
    },
    "011c" : {
      "tag" : "PlanarConfiguration",
      "description" : "画像データの並び",
      "mean" : {
        "1" : "点順次フォーマット",
        "2" : "面順次フォーマット",
      }
    },
    "011d" : {
      "tag" : "PageName",
      "description" : "???"
    },
    "011e" : {
      "tag" : "XPosition",
      "description" : "???"
    },
    "011f" : {
      "tag" : "YPosition",
      "description" : "???"
    },
    "0120" : {
      "tag" : "FreeOffsets",
      "description" : "???"
    },
    "0121" : {
      "tag" : "FreeByteCounts",
      "description" : "???"
    },
    "0122" : {
      "tag" : "GrayResponseUnit",
      "description" : "???"
    },
    "0123" : {
      "tag" : "GrayResponseCurve",
      "description" : "???"
    },
    "0124" : {
      "tag" : "T4Options",
      "description" : "???"
    },
    "0125" : {
      "tag" : "T6Options",
      "description" : "???"
    },
    "0128" : {
      "tag" : "ResolutionUnit",
      "description" : "画像の幅と高さの解像度の単位",
      "mean" : {
        "2" : "インチ",
        "3" : "センチメートル",
      }
    },
    "0129" : {
      "tag" : "PageNumber",
      "description" : "???"
    },
    "012c" : {
      "tag" : "ColorResponseUnit",
      "description" : "???"
    },
    "012d" : {
      "tag" : "TransferFunction",
      "description" : "再生階調カーブ特性"
    },
    "0131" : {
      "tag" : "Software",
      "description" : "ソフトウェア"
    },
    "0132" : {
      "tag" : "DateTime",
      "description" : "ファイル変更日時"
    },
    "013b" : {
      "tag" : "Artist",
      "description" : "アーティスト"
    },
    "013c" : {
      "tag" : "HostComputer",
      "description" : "???"
    },
    "013d" : {
      "tag" : "Predictor",
      "description" : "???"
    },
    "013e" : {
      "tag" : "WhitePoint",
      "description" : "参照白色点の色度座標値"
    },
    "013f" : {
      "tag" : "PrimaryChromaticities",
      "description" : "原色の色度座標値"
    },
    "0140" : {
      "tag" : "ColorMap",
      "description" : "???"
    },
    "0141" : {
      "tag" : "HalftoneHints",
      "description" : "???"
    },
    "0142" : {
      "tag" : "TileWidth",
      "description" : "???"
    },
    "0143" : {
      "tag" : "TileLength",
      "description" : "???"
    },
    "0144" : {
      "tag" : "TileOffsets",
      "description" : "???"
    },
    "0145" : {
      "tag" : "TileByteCounts",
      "description" : "???"
    },
    "0146" : {
      "tag" : "BadFaxLines",
      "description" : "???"
    },
    "0147" : {
      "tag" : "CleanFaxData",
      "description" : "???"
    },
    "0148" : {
      "tag" : "ConsecutiveBadFaxLines",
      "description" : "???"
    },
    "014a" : {
      "tag" : "SubIFD",
      "description" : "???"
    },
    "014c" : {
      "tag" : "InkSet",
      "description" : "???"
    },
    "014d" : {
      "tag" : "InkNames",
      "description" : "???"
    },
    "014e" : {
      "tag" : "NumberofInks",
      "description" : "???"
    },
    "0150" : {
      "tag" : "DotRange",
      "description" : "???"
    },
    "0151" : {
      "tag" : "TargetPrinter",
      "description" : "???"
    },
    "0152" : {
      "tag" : "ExtraSamples",
      "description" : "???"
    },
    "0153" : {
      "tag" : "SampleFormat",
      "description" : "???"
    },
    "0154" : {
      "tag" : "SMinSampleValue",
      "description" : "???"
    },
    "0155" : {
      "tag" : "SMaxSampleValue",
      "description" : "???"
    },
    "0156" : {
      "tag" : "TransferRange",
      "description" : "???"
    },
    "0157" : {
      "tag" : "ClipPath",
      "description" : "???"
    },
    "0158" : {
      "tag" : "XClipPathUnits",
      "description" : "???"
    },
    "0159" : {
      "tag" : "YClipPathUnits",
      "description" : "???"
    },
    "015a" : {
      "tag" : "Indexed",
      "description" : "???"
    },
    "015b" : {
      "tag" : "JPEGTables",
      "description" : "???"
    },
    "015f" : {
      "tag" : "OPIProxy",
      "description" : "???"
    },
    "0190" : {
      "tag" : "GlobalParametersIFD",
      "description" : "???"
    },
    "0191" : {
      "tag" : "ProfileType",
      "description" : "???"
    },
    "0192" : {
      "tag" : "FaxProfile",
      "description" : "???"
    },
    "0193" : {
      "tag" : "CodingMethods",
      "description" : "???"
    },
    "0194" : {
      "tag" : "VersionYear",
      "description" : "???"
    },
    "0195" : {
      "tag" : "ModeNumber",
      "description" : "???"
    },
    "01b1" : {
      "tag" : "Decode",
      "description" : "???"
    },
    "01b2" : {
      "tag" : "DefaultImageColor",
      "description" : "???"
    },
    "01b3" : {
      "tag" : "T82Options",
      "description" : "???"
    },
    "01b5" : {
      "tag" : "JPEGTables",
      "description" : "???"
    },
    "0200" : {
      "tag" : "JPEGProc",
      "description" : "???"
    },
    "0201" : {
      "tag" : "JPEGInterchangeFormat",
      "description" : "JPEGのSOIへのオフセット"
    },
    "0202" : {
      "tag" : "JPEGInterchangeFormatLength",
      "description" : "JPEGデータのバイト数"
    },

    "0203" : {
      "tag" : "JPEGRestartInterval",
      "description" : "???"
    },
    "0205" : {
      "tag" : "JPEGLosslessPredictors",
      "description" : "???"
    },
    "0206" : {
      "tag" : "JPEGPointTransforms",
      "description" : "???"
    },
    "0207" : {
      "tag" : "JPEGQTables",
      "description" : "???"
    },
    "0208" : {
      "tag" : "JPEGDCTables",
      "description" : "???"
    },
    "0209" : {
      "tag" : "JPEGACTables",
      "description" : "???"
    },
    "0211" : {
      "tag" : "YCbCrCoefficients",
      "description" : "色変換マトリクス係数"
    },
    "0212" : {
      "tag" : "YCbCrSubSampling",
      "description" : "YCCの画素構成(Cの間引き率)",
      "mean" : {
        "2,1" : "YCbCr 4:2:2",
        "2,2" : "YCbCr 4:2:0",
      }
    },
    "0213" : {
      "tag" : "YCbCrPositioning",
      "description" : "YCCの画素構成(YとCの位置)",
      "mean" : {
        "1" : "中心",
        "2" : "一致",
      }
    },
    "0214" : {
      "tag" : "ReferenceBlackWhite",
      "description" : "参照黒色点値と参照白色点値"
    },
    "022f" : {
      "tag" : "StripRowCounts",
      "description" : "???"
    },
    "02bc" : {
      "tag" : "ApplicationNotes",
      "description" : "???"
    },
    "03e7" : {
      "tag" : "USPTOMiscellaneous",
      "description" : "???"
    },
    "1000" : {
      "tag" : "RelatedImageFileFormat",
      "description" : "???"
    },
    "1001" : {
      "tag" : "RelatedImageWidth",
      "description" : "???"
    },
    "1002" : {
      "tag" : "RelatedImageHeight",
      "description" : "???"
    },
    "4746" : {
      "tag" : "Rating",
      "description" : "???"
    },
    "4747" : {
      "tag" : "XP",
      "description" : "???"
    },
    "4748" : {
      "tag" : "StitchInfo",
      "description" : "???"
    },
    "4749" : {
      "tag" : "RatingPercent",
      "description" : "???"
    },
    "7000" : {
      "tag" : "SonyRawFileType",
      "description" : "???"
    },
    "7035" : {
      "tag" : "ChromaticAberrationCorrParams",
      "description" : "???"
    },
    "7037" : {
      "tag" : "DistortionCorrParams",
      "description" : "???"
    },
    "800d" : {
      "tag" : "ImageID",
      "description" : "???"
    },
    "80a3" : {
      "tag" : "WangTag1",
      "description" : "???"
    },
    "80a4" : {
      "tag" : "WangAnnotation",
      "description" : "???"
    },
    "80a5" : {
      "tag" : "WangTag3",
      "description" : "???"
    },
    "80a6" : {
      "tag" : "WangTag4",
      "description" : "???"
    },
    "80b8" : {
      "tag" : "ImageReferencePoints",
      "description" : "???"
    },
    "80b9" : {
      "tag" : "RegionXformTackPoint",
      "description" : "???"
    },
    "80ba" : {
      "tag" : "WarpQuadrilateral",
      "description" : "???"
    },
    "80bb" : {
      "tag" : "AffineTransformMat",
      "description" : "???"
    },
    "80e3" : {
      "tag" : "Matteing",
      "description" : "???"
    },
    "80e4" : {
      "tag" : "DataType",
      "description" : "???"
    },
    "80e5" : {
      "tag" : "ImageDepth",
      "description" : "???"
    },
    "80e6" : {
      "tag" : "TileDepth",
      "description" : "???"
    },
    "8214" : {
      "tag" : "ImageFullWidth",
      "description" : "???"
    },
    "8215" : {
      "tag" : "ImageFullHeight",
      "description" : "???"
    },
    "8216" : {
      "tag" : "TextureFormat",
      "description" : "???"
    },
    "8217" : {
      "tag" : "WrapModes",
      "description" : "???"
    },
    "8218" : {
      "tag" : "FovCot",
      "description" : "???"
    },
    "8219" : {
      "tag" : "MatrixWorldToScreen",
      "description" : "???"
    },
    "821a" : {
      "tag" : "MatrixWorldToCamera",
      "description" : "???"
    },
    "827d" : {
      "tag" : "Model2",
      "description" : "???"
    },
    "828d" : {
      "tag" : "CFARepeatPatternDim",
      "description" : "???"
    },
    "828e" : {
      "tag" : "CFAPattern2",
      "description" : "???"
    },
    "828f" : {
      "tag" : "BatteryLevel",
      "description" : "???"
    },
    "8290" : {
      "tag" : "KodakIFD",
      "description" : "???"
    },

    "8298" : {
      "tag" : "Copyright",
      "description" : "撮影著作権者/編集著作権者"
    },

    "82a5" : {
      "tag" : "MDFileTag",
      "description" : "???"
    },
    "82a6" : {
      "tag" : "MDScalePixel",
      "description" : "???"
    },
    "82a7" : {
      "tag" : "MDColorTable",
      "description" : "???"
    },
    "82a8" : {
      "tag" : "MDLabName",
      "description" : "???"
    },
    "82a9" : {
      "tag" : "MDSampleInfo",
      "description" : "???"
    },
    "82aa" : {
      "tag" : "MDPrepDate",
      "description" : "???"
    },
    "82ab" : {
      "tag" : "MDPrepTime",
      "description" : "???"
    },
    "82ac" : {
      "tag" : "MDFileUnits",
      "description" : "???"
    },
    "830e" : {
      "tag" : "PixelScale",
      "description" : "???"
    },
    "8335" : {
      "tag" : "AdventScale",
      "description" : "???"
    },
    "8336" : {
      "tag" : "AdventRevision",
      "description" : "???"
    },
    "835c" : {
      "tag" : "UIC1Tag",
      "description" : "???"
    },
    "835d" : {
      "tag" : "UIC2Tag",
      "description" : "???"
    },
    "835e" : {
      "tag" : "UIC3Tag",
      "description" : "???"
    },
    "835f" : {
      "tag" : "UIC4Tag",
      "description" : "???"
    },
    "83bb" : {
      "tag" : "IPTC",
      "description" : "???"
    },
    "847e" : {
      "tag" : "IntergraphPacketData",
      "description" : "???"
    },
    "847f" : {
      "tag" : "IntergraphFlagRegisters",
      "description" : "???"
    },
    "8480" : {
      "tag" : "IntergraphMatrix",
      "description" : "???"
    },
    "8481" : {
      "tag" : "INGRReserved",
      "description" : "???"
    },
    "8482" : {
      "tag" : "ModelTiePoint",
      "description" : "???"
    },
    "84e0" : {
      "tag" : "sITE",
      "description" : "???"
    },
    "84e1" : {
      "tag" : "ColorSequence",
      "description" : "???"
    },
    "84e2" : {
      "tag" : "IT8Header",
      "description" : "???"
    },
    "84e3" : {
      "tag" : "RasterPadding",
      "description" : "???"
    },
    "84e4" : {
      "tag" : "BitsPerRunLength",
      "description" : "???"
    },
    "84e5" : {
      "tag" : "BitsPerExtendedRunLength",
      "description" : "???"
    },
    "84e6" : {
      "tag" : "ColorTable",
      "description" : "???"
    },
    "84e7" : {
      "tag" : "ImageColorIndicator",
      "description" : "???"
    },
    "84e8" : {
      "tag" : "BackgroundColorIndicator",
      "description" : "???"
    },
    "84e9" : {
      "tag" : "ImageColorValue",
      "description" : "???"
    },
    "84ea" : {
      "tag" : "BackgroundColorValue",
      "description" : "???"
    },
    "84eb" : {
      "tag" : "PixelIntensityRange",
      "description" : "???"
    },
    "84ec" : {
      "tag" : "TransparencyIndicator",
      "description" : "???"
    },
    "84ed" : {
      "tag" : "ColorCharacterization",
      "description" : "???"
    },
    "84ee" : {
      "tag" : "HCUsage",
      "description" : "???"
    },
    "84ef" : {
      "tag" : "TrapIndicator",
      "description" : "???"
    },
    "84f0" : {
      "tag" : "CMYKEquivalent",
      "description" : "???"
    },
    "8546" : {
      "tag" : "SEMInfo",
      "description" : "???"
    },
    "8568" : {
      "tag" : "afcp",
      "description" : "???"
    },
    "85b8" : {
      "tag" : "PixelMagicJBIGOptions",
      "description" : "???"
    },
    "85d7" : {
      "tag" : "JPLCartoIFD",
      "description" : "???"
    },
    "85d8" : {
      "tag" : "ModelTransform",
      "description" : "???"
    },
    "8602" : {
      "tag" : "WB",
      "description" : "???"
    },
    "8606" : {
      "tag" : "LeafData",
      "description" : "???"
    },
    "8649" : {
      "tag" : "PhotoshopSettings",
      "description" : "???"
    },
    "8769" : {
      "tag" : "Exif IFD Pointer",
      "description" : "Exifタグ"
    },
    "8773" : {
      "tag" : "ICC",
      "description" : "???"
    },
    "877f" : {
      "tag" : "tiff",
      "description" : "???"
    },
    "8780" : {
      "tag" : "MultiProfiles",
      "description" : "???"
    },
    "8781" : {
      "tag" : "SharedData",
      "description" : "???"
    },
    "8782" : {
      "tag" : "T88Options",
      "description" : "???"
    },
    "87ac" : {
      "tag" : "ImageLayer",
      "description" : "???"
    },
    "87af" : {
      "tag" : "GeoTiffDirectory",
      "description" : "???"
    },
    "87b0" : {
      "tag" : "GeoTiffDoubleParams",
      "description" : "???"
    },
    "87b1" : {
      "tag" : "GeoTiffAsciiParams",
      "description" : "???"
    },
    "87be" : {
      "tag" : "JBIGOptions",
      "description" : "???"
    },

    "8822" : {
      "tag" : "ExposureProgram",
      "description" : "露出プログラム",
      "mean" : {
        "0" : "未定義",
        "1" : "マニュアル",
        "2" : "ノーマルプログラム",
        "3" : "絞り優先",
        "4" : "シャッター優先",
        "5" : "creativeプログラム(被写界深度)",
        "6" : "actionプログラム(シャッタースピード)",
        "7" : "ポートレイトモード(クローズアップ撮影、背景はフォーカスを外す)",
        "8" : "ランドスケープモード(landscape撮影、背景はフォーカス合う)",
      }
    },
    "8824" : {
      "tag" : "SpectralSensitivity",
      "description" : "スペクトル感度"
    },

    "8825" : {
      "tag" : "GPSInfo IFD Pointer",
      "description" : "GPSタグ"
    },
    "8827" : {
      "tag" : "PhotographicSensitivity",
      "description" : "撮影感度"
    },
    "8828" : {
      "tag" : "OECF",
      "description" : "光電変換関数"
    },

    "8829" : {
      "tag" : "Interlace",
      "description" : "???"
    },
    "882a" : {
      "tag" : "TimeZoneOffset",
      "description" : "???"
    },
    "882b" : {
      "tag" : "SelfTimerMode",
      "description" : "???"
    },
    "829a" : {
      "tag" : "ExposureTime",
      "description" : "露出時間"
    },
    "829d" : {
      "tag" : "FNumber",
      "description" : "Fナンバー"
    },
    "8830" : {
      "tag" : "SensitivityType",
      "description" : "感度種別"
    },
    "8831" : {
      "tag" : "StandardOutputSensitivity",
      "description" : "標準出力感度"
    },
    "8832" : {
      "tag" : "RecommendedExposureIndex",
      "description" : "推奨露光指数"
    },
    "8833" : {
      "tag" : "ISOSpeed",
      "description" : "ISOスピード"
    },
    "8834" : {
      "tag" : "ISOSpeedLatitudeyyy",
      "description" : "ISOスピードラチチュードyyy"
    },
    "8835" : {
      "tag" : "ISOSpeedLatitudezzz",
      "description" : "ISOスピードラチチュードzzz"
    },

    "885c" : {
      "tag" : "FaxRecvParams",
      "description" : "???"
    },
    "885d" : {
      "tag" : "FaxSubAddress",
      "description" : "???"
    },
    "885e" : {
      "tag" : "FaxRecvTime",
      "description" : "???"
    },
    "8871" : {
      "tag" : "FedexEDR",
      "description" : "???"
    },
    "888a" : {
      "tag" : "LeafSubIFD",
      "description" : "???"
    },

    "9000" : {
      "tag" : "ExifVersion",
      "description" : "Exifバージョン"
    },
    "9003" : {
      "tag" : "DateTimeOriginal",
      "description" : "原画像データの生成日時"
    },
    "9004" : {
      "tag" : "DateTimeDigitized",
      "description" : "デジタルデータの作成日時"
    },
    "9009" : {
      "tag" : "GooglePlusUploadCode",
      "description" : "???"
    },

    "9101" : {
      "tag" : "ComponentsConfiguration",
      "description" : "各コンポーネントの意味",
      "mean" : {
        "0" : "存在しない",
        "1" : "Y",
        "2" : "Cb",
        "3" : "Cr",
        "4" : "R",
        "5" : "G",
        "6" : "B",
      }
    },
    "9102" : {
      "tag" : "CompressedBitsPerPixel",
      "description" : "画像圧縮モード"
    },
    "9201" : {
      "tag" : "ShutterSpeedValue",
      "description" : "シャッタースピード"
    },
    "9202" : {
      "tag" : "ApertureValue",
      "description" : "絞り値"
    },
    "9203" : {
      "tag" : "BrightnessValue",
      "description" : "輝度値"
    },
    "9204" : {
      "tag" : "ExposureBiasValue",
      "description" : "露光補正値"
    },
    "9205" : {
      "tag" : "MaxApertureValue",
      "description" : "レンズ最小Ｆ値"
    },
    "9206" : {
      "tag" : "SubjectDistance",
      "description" : "被写体距離"
    },
    "9207" : {
      "tag" : "MeteringMode",
      "description" : "測光方式"
    },
    "9208" : {
      "tag" : "LightSource",
      "description" : "光源"
    },
    "9209" : {
      "tag" : "Flash",
      "description" : "フラッシュ"
    },
    "920a" : {
      "tag" : "FocalLength",
      "description" : "レンズ焦点距離"
    },

    "920b" : {
      "tag" : "FlashEnergy",
      "description" : "???"
    },
    "920c" : {
      "tag" : "SpatialFrequencyResponse",
      "description" : "???"
    },
    "920d" : {
      "tag" : "Noise",
      "description" : "???"
    },
    "920e" : {
      "tag" : "FocalPlaneXResolution",
      "description" : "???"
    },
    "920f" : {
      "tag" : "FocalPlaneYResolution",
      "description" : "???"
    },
    "9210" : {
      "tag" : "FocalPlaneResolutionUnit",
      "description" : "???"
    },
    "9211" : {
      "tag" : "ImageNumber",
      "description" : "???"
    },
    "9212" : {
      "tag" : "SecurityClassification",
      "description" : "???"
    },
    "9213" : {
      "tag" : "ImageHistory",
      "description" : "???"
    },

    "9214" : {
      "tag" : "SubjectArea",
      "description" : "被写体領域"
    },

    "9215" : {
      "tag" : "ExposureIndex",
      "description" : "???"
    },
    "9216" : {
      "tag" : "Tiff",
      "description" : "???"
    },
    "9217" : {
      "tag" : "SensingMethod",
      "description" : "???"
    },

    "923a" : {
      "tag" : "CIP3DataFile",
      "description" : "???"
    },
    "923b" : {
      "tag" : "CIP3Sheet",
      "description" : "???"
    },
    "923c" : {
      "tag" : "CIP3Side",
      "description" : "???"
    },
    "923f" : {
      "tag" : "StoNits",
      "description" : "???"
    },
    "927c" : {
      "tag" : "MakerNote",
      "description" : "メーカノート"
    },
    "9286" : {
      "tag" : "UserComment",
      "description" : "ユーザコメント"
    },
    "9290" : {
      "tag" : "SubSecTime",
      "description" : "DateTimeのサブセック"
    },
    "9291" : {
      "tag" : "SubSecTimeOriginal",
      "description" : "DateTimeOriginalのサブセック"
    },
    "9292" : {
      "tag" : "SubSecTimeDigitized",
      "description" : "DateTimeDigitizedのサブセック"
    },

    "932f" : {
      "tag" : "MSDocumentText",
      "description" : "???"
    },
    "9330" : {
      "tag" : "MSPropertySetStorage",
      "description" : "???"
    },
    "9331" : {
      "tag" : "MSDocumentTextPosition",
      "description" : "???"
    },
    "935c" : {
      "tag" : "ImageSourceData",
      "description" : "???"
    },
    "9c9b" : {
      "tag" : "XPTitle",
      "description" : "???"
    },
    "9c9c" : {
      "tag" : "XPComment",
      "description" : "???"
    },
    "9c9d" : {
      "tag" : "XPAuthor",
      "description" : "???"
    },
    "9c9e" : {
      "tag" : "XPKeywords",
      "description" : "???"
    },
    "9c9f" : {
      "tag" : "XPSubject",
      "description" : "???"
    },
    "a20d" : {
      "tag" : "Noise",
      "description" : "???"
    },
    "a211" : {
      "tag" : "ImageNumber",
      "description" : "???"
    },
    "a212" : {
      "tag" : "SecurityClassification",
      "description" : "???"
    },
    "a213" : {
      "tag" : "ImageHistory",
      "description" : "???"
    },
    "a216" : {
      "TAG" : "TIFF",
      "description" : "???"
    },
    "a480" : {
      "tag" : "GDALMetadata",
      "description" : "???"
    },
    "a481" : {
      "tag" : "GDALNoData",
      "description" : "???"
    },
    "afc0" : {
      "tag" : "ExpandSoftware",
      "description" : "???"
    },
    "afc1" : {
      "tag" : "ExpandLens",
      "description" : "???"
    },
    "afc2" : {
      "tag" : "ExpandFilm",
      "description" : "???"
    },
    "afc3" : {
      "tag" : "ExpandFilterLens",
      "description" : "???"
    },
    "afc4" : {
      "tag" : "ExpandScanner",
      "description" : "???"
    },
    "afc5" : {
      "tag" : "ExpandFlashLamp",
      "description" : "???"
    },

    "a000" : {
      "tag" : "FlashpixVersion",
      "description" : "対応フラッシュピックスバージョン",
      "mean" : {
        "0100" : "fLASHPIX fORMAT vERSION 1.0",
      }
    },
    "a001" : {
      "tag" : "ColorSpace",
      "description" : "色空間情報",
      "mean" : {
        "1" : "sRGB",
        "ffff" : "uNCALIBRATED",
      }
    },
    "a002" : {
      "tag" : "PixelXDimension",
      "description" : "実効画像幅"
    },
    "a003" : {
      "tag" : "PixelYDimension",
      "description" : "実効画像高さ"
    },
    "a004" : {
      "tag" : "RelatedSoundFile",
      "description" : "関連音声ファイル"
    },
    "a005" : {
      "tag" : "Interoperability IFD Pointer",
      "description" : "互換性IFDへのポインタ"
    },
    "a20b" : {
      "tag" : "FlashEnergy",
      "description" : "フラッシュ強度"
    },
    "a20c" : {
      "tag" : "SpatialFrequencyResponse",
      "description" : "空間周波数応答"
    },
    "a20e" : {
      "tag" : "FocalPlaneXResolution",
      "description" : "焦点面の幅の解像度"
    },
    "a20f" : {
      "tag" : "FocalPlaneYResolution",
      "description" : "焦点面の高さの解像度"
    },
    "a210" : {
      "tag" : "FocalPlaneResolutionUnit",
      "description" : "焦点面解像度単位"
    },
    "a214" : {
      "tag" : "SubjectLocation",
      "description" : "被写体位置"
    },
    "a215" : {
      "tag" : "ExposureIndex",
      "description" : "露出インデックス"
    },
    "a217" : {
      "tag" : "SensingMethod",
      "description" : "センサ方式"
    },
    "a300" : {
      "tag" : "FileSource",
      "description" : "ファイルソース"
    },
    "a301" : {
      "tag" : "SceneType",
      "description" : "シーンタイプ"
    },
    "a302" : {
      "tag" : "CFAPattern",
      "description" : "CFAパターン"
    },
    "a401" : {
      "tag" : "CustomRendered",
      "description" : "個別画像処理"
    },
    "a402" : {
      "tag" : "ExposureMode",
      "description" : "露出モード"
    },
    "a403" : {
      "tag" : "WhiteBalance",
      "description" : "ホワイトバランス"
    },
    "a404" : {
      "tag" : "DigitalZoomRatio",
      "description" : "デジタルズーム倍率"
    },
    "a405" : {
      "tag" : "FocalLengthIn35mmFilm",
      "description" : "35mm換算レンズ焦点距離"
    },
    "a406" : {
      "tag" : "SceneCaptureType",
      "description" : "撮影シーンタイプ"
    },
    "a407" : {
      "tag" : "GainControl",
      "description" : "ゲイン制御"
    },
    "a408" : {
      "tag" : "Contrast",
      "description" : "撮影コントラスト"
    },
    "a409" : {
      "tag" : "Saturation",
      "description" : "撮影彩度"
    },
    "a40a" : {
      "tag" : "Sharpness",
      "description" : "撮影シャープネス"
    },
    "a40b" : {
      "tag" : "DeviceSettingDescription",
      "description" : "撮影条件記述情報"
    },
    "a40c" : {
      "tag" : "SubjectDistanceRange",
      "description" : "被写体距離レンジ"
    },
    "a420" : {
      "tag" : "ImageUniqueID",
      "description" : "画像ユニークID"
    },
    "a430" : {
      "tag" : "CameraOwnerName",
      "description" : "カメラ所有者名"
    },
    "a431" : {
      "tag" : "BodySerialNumber",
      "description" : "カメラシリアル番号"
    },
    "a432" : {
      "tag" : "LensSpecification",
      "description" : "レンズの仕様情報"
    },
    "a433" : {
      "tag" : "LensMake",
      "description" : "レンズのメーカ名"
    },
    "a434" : {
      "tag" : "LensModel",
      "description" : "レンズのモデル名"
    },
    "a435" : {
      "tag" : "LensSerialNumber",
      "description" : "レンズシリアル番号"
    },
    "a500" : {
      "tag" : "Gamma",
      "description" : "再生ガンマ"
    },
    "bc01" : {
      "tag" : "PixelFormat",
      "description" : "???"
    },
    "bc02" : {
      "tag" : "Transformation",
      "description" : "???"
    },
    "bc03" : {
      "tag" : "Uncompressed",
      "description" : "???"
    },
    "bc04" : {
      "tag" : "ImageType",
      "description" : "???"
    },
    "bc80" : {
      "tag" : "ImageWidth",
      "description" : "???"
    },
    "bc81" : {
      "tag" : "ImageHeight",
      "description" : "???"
    },
    "bc82" : {
      "tag" : "WidthResolution",
      "description" : "???"
    },
    "bc83" : {
      "tag" : "HeightResolution",
      "description" : "???"
    },
    "bcc0" : {
      "tag" : "ImageOffset",
      "description" : "???"
    },
    "bcc1" : {
      "tag" : "ImageByteCount",
      "description" : "???"
    },
    "bcc2" : {
      "tag" : "AlphaOffset",
      "description" : "???"
    },
    "bcc3" : {
      "tag" : "AlphaByteCount",
      "description" : "???"
    },
    "bcc4" : {
      "tag" : "ImageDataDiscard",
      "description" : "???"
    },
    "bcc5" : {
      "tag" : "AlphaDataDiscard",
      "description" : "???"
    },
    "c427" : {
      "tag" : "OceScanjobDesc",
      "description" : "???"
    },
    "c428" : {
      "tag" : "OceApplicationSelector",
      "description" : "???"
    },
    "c429" : {
      "tag" : "OceIDNumber",
      "description" : "???"
    },
    "c42a" : {
      "tag" : "OceImageLogic",
      "description" : "???"
    },
    "c44f" : {
      "tag" : "Annotations",
      "description" : "???"
    },
    "c4a5" : {
      "tag" : "PrintIM",
      "description" : "???"
    },
    "c573" : {
      "tag" : "OriginalFileName",
      "description" : "???"
    },
    "c580" : {
      "tag" : "USPTOOriginalContentType",
      "description" : "???"
    },
    "c612" : {
      "tag" : "DNGVersion",
      "description" : "???"
    },
    "c613" : {
      "tag" : "DNGBackwardVersion",
      "description" : "???"
    },
    "c614" : {
      "tag" : "UniqueCameraModel",
      "description" : "???"
    },
    "c615" : {
      "tag" : "LocalizedCameraModel",
      "description" : "???"
    },
    "c616" : {
      "tag" : "CFAPlaneColor",
      "description" : "???"
    },
    "c617" : {
      "tag" : "CFALayout",
      "description" : "???"
    },
    "c618" : {
      "tag" : "LinearizationTable",
      "description" : "???"
    },
    "c619" : {
      "tag" : "BlackLevelRepeatDim",
      "description" : "???"
    },
    "c61a" : {
      "tag" : "BlackLevel",
      "description" : "???"
    },
    "c61b" : {
      "tag" : "BlackLevelDeltaH",
      "description" : "???"
    },
    "c61c" : {
      "tag" : "BlackLevelDeltaV",
      "description" : "???"
    },
    "c61d" : {
      "tag" : "WhiteLevel",
      "description" : "???"
    },
    "c61e" : {
      "tag" : "DefaultScale",
      "description" : "???"
    },
    "c61f" : {
      "tag" : "DefaultCropOrigin",
      "description" : "???"
    },
    "c620" : {
      "tag" : "DefaultCropSize",
      "description" : "???"
    },
    "c621" : {
      "tag" : "ColorMatrix1",
      "description" : "???"
    },
    "c622" : {
      "tag" : "ColorMatrix2",
      "description" : "???"
    },
    "c623" : {
      "tag" : "CameraCalibration1",
      "description" : "???"
    },
    "c624" : {
      "tag" : "CameraCalibration2",
      "description" : "???"
    },
    "c625" : {
      "tag" : "ReductionMatrix1",
      "description" : "???"
    },
    "c626" : {
      "tag" : "ReductionMatrix2",
      "description" : "???"
    },
    "c627" : {
      "tag" : "AnalogBalance",
      "description" : "???"
    },
    "c628" : {
      "tag" : "AsShotNeutral",
      "description" : "???"
    },
    "c629" : {
      "tag" : "AsShotWhiteXY",
      "description" : "???"
    },
    "c62a" : {
      "tag" : "BaselineExposure",
      "description" : "???"
    },
    "c62b" : {
      "tag" : "BaselineNoise",
      "description" : "???"
    },
    "c62c" : {
      "tag" : "BaselineSharpness",
      "description" : "???"
    },
    "c62d" : {
      "tag" : "BayerGreenSplit",
      "description" : "???"
    },
    "c62e" : {
      "tag" : "LinearResponseLimit",
      "description" : "???"
    },
    "c62f" : {
      "tag" : "CameraSerialNumber",
      "description" : "???"
    },
    "c630" : {
      "tag" : "DNGLensInfo",
      "description" : "???"
    },
    "c631" : {
      "tag" : "ChromaBlurRadius",
      "description" : "???"
    },
    "c632" : {
      "tag" : "AntiAliasStrength",
      "description" : "???"
    },
    "c633" : {
      "tag" : "ShadowScale",
      "description" : "???"
    },
    "c634" : {
      "tag" : "SR2Private",
      "description" : "???"
    },
    "c635" : {
      "tag" : "MakerNoteSafety",
      "description" : "???"
    },
    "c640" : {
      "tag" : "RawImageSegmentation",
      "description" : "???"
    },
    "c65a" : {
      "tag" : "CalibrationIlluminant1",
      "description" : "???"
    },
    "c65b" : {
      "tag" : "CalibrationIlluminant2",
      "description" : "???"
    },
    "c65c" : {
      "tag" : "BestQualityScale",
      "description" : "???"
    },
    "c65d" : {
      "tag" : "RawDataUniqueID",
      "description" : "???"
    },
    "c660" : {
      "tag" : "AliasLayerMetadata",
      "description" : "???"
    },
    "c68b" : {
      "tag" : "OriginalRawFileName",
      "description" : "???"
    },
    "c68c" : {
      "tag" : "OriginalRawFileData",
      "description" : "???"
    },
    "c68d" : {
      "tag" : "ActiveArea",
      "description" : "???"
    },
    "c68e" : {
      "tag" : "MaskedAreas",
      "description" : "???"
    },
    "c68f" : {
      "tag" : "AsShotICCProfile",
      "description" : "???"
    },
    "c690" : {
      "tag" : "AsShotPreProfileMatrix",
      "description" : "???"
    },
    "c691" : {
      "tag" : "CurrentICCProfile",
      "description" : "???"
    },
    "c692" : {
      "tag" : "CurrentPreProfileMatrix",
      "description" : "???"
    },
    "c6bf" : {
      "tag" : "ColorimetricReference",
      "description" : "???"
    },
    "c6c5" : {
      "tag" : "SRawType",
      "description" : "???"
    },
    "c6d2" : {
      "tag" : "PanasonicTitle",
      "description" : "???"
    },
    "c6d3" : {
      "tag" : "PanasonicTitle2",
      "description" : "???"
    },
    "c6f3" : {
      "tag" : "CameraCalibrationSig",
      "description" : "???"
    },
    "c6f4" : {
      "tag" : "ProfileCalibrationSig",
      "description" : "???"
    },
    "c6f5" : {
      "tag" : "ProfileIFD",
      "description" : "???"
    },
    "c6f6" : {
      "tag" : "AsShotProfileName",
      "description" : "???"
    },
    "c6f7" : {
      "tag" : "NoiseReductionApplied",
      "description" : "???"
    },
    "c6f8" : {
      "tag" : "ProfileName",
      "description" : "???"
    },
    "c6f9" : {
      "tag" : "ProfileHueSatMapDims",
      "description" : "???"
    },
    "c6fa" : {
      "tag" : "ProfileHueSatMapData1",
      "description" : "???"
    },
    "c6fb" : {
      "tag" : "ProfileHueSatMapData2",
      "description" : "???"
    },
    "c6fc" : {
      "tag" : "ProfileToneCurve",
      "description" : "???"
    },
    "c6fd" : {
      "tag" : "ProfileEmbedPolicy",
      "description" : "???"
    },
    "c6fe" : {
      "tag" : "ProfileCopyright",
      "description" : "???"
    },
    "c714" : {
      "tag" : "ForwardMatrix1",
      "description" : "???"
    },
    "c715" : {
      "tag" : "ForwardMatrix2",
      "description" : "???"
    },
    "c716" : {
      "tag" : "PreviewApplicationName",
      "description" : "???"
    },
    "c717" : {
      "tag" : "PreviewApplicationVersion",
      "description" : "???"
    },
    "c718" : {
      "tag" : "PreviewSettingsName",
      "description" : "???"
    },
    "c719" : {
      "tag" : "PreviewSettingsDigest",
      "description" : "???"
    },
    "c71a" : {
      "tag" : "PreviewColorSpace",
      "description" : "???"
    },
    "c71b" : {
      "tag" : "PreviewDateTime",
      "description" : "???"
    },
    "c71c" : {
      "tag" : "RawImageDigest",
      "description" : "???"
    },
    "c71d" : {
      "tag" : "OriginalRawFileDigest",
      "description" : "???"
    },
    "c71e" : {
      "tag" : "SubTileBlockSize",
      "description" : "???"
    },
    "c71f" : {
      "tag" : "RowInterleaveFactor",
      "description" : "???"
    },
    "c725" : {
      "tag" : "ProfileLookTableDims",
      "description" : "???"
    },
    "c726" : {
      "tag" : "ProfileLookTableData",
      "description" : "???"
    },
    "c740" : {
      "tag" : "OpcodeList1",
      "description" : "???"
    },
    "c741" : {
      "tag" : "OpcodeList2",
      "description" : "???"
    },
    "c74e" : {
      "tag" : "OpcodeList3",
      "description" : "???"
    },
    "c761" : {
      "tag" : "NoiseProfile",
      "description" : "???"
    },
    "c763" : {
      "tag" : "TimeCodes",
      "description" : "???"
    },
    "c764" : {
      "tag" : "FrameRate",
      "description" : "???"
    },
    "c772" : {
      "tag" : "TStop",
      "description" : "???"
    },
    "c789" : {
      "tag" : "ReelName",
      "description" : "???"
    },
    "c791" : {
      "tag" : "OriginalDefaultFinalSize",
      "description" : "???"
    },
    "c792" : {
      "tag" : "OriginalBestQualitySize",
      "description" : "???"
    },
    "c793" : {
      "tag" : "OriginalDefaultCropSize",
      "description" : "???"
    },
    "c7a1" : {
      "tag" : "CameraLabel",
      "description" : "???"
    },
    "c7a3" : {
      "tag" : "ProfileHueSatMapEncoding",
      "description" : "???"
    },
    "c7a4" : {
      "tag" : "ProfileLookTableEncoding",
      "description" : "???"
    },
    "c7a5" : {
      "tag" : "BaselineExposureOffset",
      "description" : "???"
    },
    "c7a6" : {
      "tag" : "DefaultBlackRender",
      "description" : "???"
    },
    "c7a7" : {
      "tag" : "NewRawImageDigest",
      "description" : "???"
    },
    "c7a8" : {
      "tag" : "RawToPreviewGain",
      "description" : "???"
    },
    "c7b5" : {
      "tag" : "DefaultUserCrop",
      "description" : "???"
    },
    "ea1c" : {
      "tag" : "Padding",
      "description" : "???"
    },
    "ea1d" : {
      "tag" : "OffsetSchema",
      "description" : "???"
    },
    "fde8" : {
      "tag" : "OwnerName",
      "description" : "???"
    },
    "fde9" : {
      "tag" : "SerialNumber",
      "description" : "???"
    },
    "fdea" : {
      "tag" : "lENS",
      "description" : "???"
    },
    "fe00" : {
      "tag" : "KDC",
      "description" : "???"
    },
    "fe4c" : {
      "tag" : "RawFile",
      "description" : "???"
    },
    "fe4d" : {
      "tag" : "Converter",
      "description" : "???"
    },
    "fe4e" : {
      "tag" : "WhiteBalance",
      "description" : "???"
    },
    "fe51" : {
      "tag" : "Exposure",
      "description" : "???"
    },
    "fe52" : {
      "tag" : "Shadows",
      "description" : "???"
    },
    "fe53" : {
      "tag" : "Brightness",
      "description" : "???"
    },
    "fe54" : {
      "tag" : "Contrast",
      "description" : "???"
    },
    "fe55" : {
      "tag" : "Saturation",
      "description" : "???"
    },
    "fe56" : {
      "tag" : "Sharpness",
      "description" : "???"
    },
    "fe57" : {
      "tag" : "Smoothness",
      "description" : "???"
    },
    "fe58" : {
      "tag" : "MoireFilter",
      "description" : "???"
    },
  },
  #Gpstags
  "gpstags" : {
    "0000" : {
      "tag" : "GPSVersionID",
      "description" : "GPSタグのバージョン"
    },
    "0001" : {
      "tag" : "GPSLatitudeRef",
      "description" : "北緯(N) or 南緯(S)"
    },
    "0002" : {
      "tag" : "GPSLatitude",
      "description" : "緯度(数値)"
    },
    "0003" : {
      "tag" : "GPSitudeRef",
      "description" : "東経(E) or 西経(W)"
    },
    "0004" : {
      "tag" : "GPSitude",
      "description" : "経度(数値)"
    },
    "0005" : {
      "tag" : "GPSAltitudeRef",
      "description" : "高度の基準"
    },
    "0006" : {
      "tag" : "GPSAltitude",
      "description" : "高度(数値)"
    },
    "0007" : {
      "tag" : "GPSTimeStamp",
      "description" : "GPS時間(原子時計の時間)"
    },
    "0008" : {
      "tag" : "GPSSatellites",
      "description" : "測位に使った衛星信号"
    },
    "0009" : {
      "tag" : "GPSStatus",
      "description" : "GPS受信機の状態"
    },
    "000a" : {
      "tag" : "GPSMeasureMode",
      "description" : "GPSの測位方法"
    },
    "000b" : {
      "tag" : "GPSDOP",
      "description" : "測位の信頼性"
    },
    "000c" : {
      "tag" : "GPSSpeedRef",
      "description" : "速度の単位"
    },
    "000d" : {
      "tag" : "GPSSpeed",
      "description" : "速度(数値)"
    },
    "000e" : {
      "tag" : "GPSTrackRef",
      "description" : "進行方向の単位"
    },
    "000f" : {
      "tag" : "GPSTrack",
      "description" : "進行方向(数値)"
    },
    "0010" : {
      "tag" : "GPSImgDirectionRef",
      "description" : "撮影した画像の方向の単位"
    },
    "0011" : {
      "tag" : "GPSImgDirection",
      "description" : "撮影した画像の方向(数値)"
    },
    "0012" : {
      "tag" : "GPSMapDatum",
      "description" : "測位に用いた地図データ"
    },
    "0013" : {
      "tag" : "GPSDestLatitudeRef",
      "description" : "目的地の北緯(N) or 南緯(S)"
    },
    "0014" : {
      "tag" : "GPSDestLatitude",
      "description" : "目的地の緯度(数値)"
    },
    "0015" : {
      "tag" : "GPSDestitudeRef",
      "description" : "目的地の東経(E) or 西経(W)"
    },
    "0016" : {
      "tag" : "GPSDestitude",
      "description" : "目的地の経度(数値)"
    },
    "0017" : {
      "tag" : "GPSDestBearingRef",
      "description" : "目的地の方角の単位"
    },
    "0018" : {
      "tag" : "GPSDestBearing",
      "description" : "目的の方角(数値)"
    },
    "0019" : {
      "tag" : "GPSDestDistanceRef",
      "description" : "目的地までの距離の単位"
    },
    "001a" : {
      "tag" : "GPSDestDistance",
      "description" : "目的地までの距離(数値)"
    },
    "001b" : {
      "tag" : "GPSProcessingMethod",
      "description" : "測位方式の名称"
    },
    "001c" : {
      "tag" : "GPSAreaInformation",
      "description" : "測位地点の名称"
    },
    "001d" : {
      "tag" : "GPSDateStamp",
      "description" : "GPS日付"
    },
    "001e" : {
      "tag" : "GPSDifferential",
      "description" : "GPS補正測位"
    },
    "001f" : {
      "tag" : "GPSHPositioningError",
      "description" : "水平方向測位誤差"
    },
  }
}

TYPE_MEAN = {
  "1" : {
    "name" : "BYTE",
    "length" : 1
  },
  "2" : {
    "name" : "ASCII",
    "length" : 1
  },
  "3" : {
    "name" : "SHORT",
    "length" : 2
  },
  "4" : {
    "name" : "LONG",
    "length" : 4
  },
  "5" : {
    "name" : "RATIONAL",
    "length" : 8
  },
  "7" : {
    "name" : "UNDEFINED",
    "length" : 1
  },
  "9" : {
    "name" : "SLONG",
    "length" : 4
  },
  "10" : {
    "name" : "SRATIONAL",
    "length" : 8
  },
  "11" : {
    "name" : "FLOAT",
    "length" : 4
  },
  "12" : {
    "name" : "DFLOAT",
    "length" : 8
  },
}
