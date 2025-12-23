# 数智法度

## 项目简介

数智法度是一个基于 Hugo 构建的法律法规文档网站，旨在为用户提供全面、结构化、易于搜索的法律法规信息。项目收集并整理了大量国家和地方的法律法规、司法解释、行政法规等，涵盖了行政执法、住建、农业农村、卫生健康、商务、城市管理、市场监管、应急管理、文化市场、民法典、生态环境、税务、自然资源等多个领域。

通过数智法度，用户可以方便地浏览、搜索和查阅各类法律法规，助力法治建设和依法行政。

## 功能特性

- **全面的法律法规资源**：涵盖行政执法、住建、农业农村、卫生健康、商务、城市管理、市场监管、应急管理、文化市场、民法典、生态环境、税务、自然资源等多个领域
- **结构化的文档组织**：按照领域、类别等进行分层组织，便于浏览和查找
- **强大的搜索功能**：支持全文搜索，方便用户快速定位所需内容
- **离线搜索支持**：通过 Lunr.js 实现离线搜索功能，无需网络连接即可搜索
- **响应式设计**：适配不同设备，提供良好的移动端体验
- **代码高亮**：支持代码块的语法高亮，便于阅读技术相关内容
- **阅读时间估算**：显示文章的预计阅读时间，帮助用户合理安排阅读
- **深色模式支持**：提供浅色/深色主题切换功能，适应不同使用场景
- **自动生成索引**：通过 Python 脚本自动生成目录索引文件，提高文档管理效率
- **自动化部署**：通过 GitHub Actions 实现自动构建和部署，确保内容及时更新

## 技术栈

### 核心框架
- **Hugo**：静态网站生成器，版本要求 0.146.0+（扩展版）
- **Docsy**：Hugo 主题，用于构建文档网站

### 前端技术
- **Bootstrap 5**：前端响应式框架
- **Font Awesome**：图标库
- **Lunr.js**：离线搜索功能
- **SCSS**：CSS 预处理器
- **PostCSS & Autoprefixer**：CSS 处理工具

### 自动化工具
- **Python 3**：用于编写自动化脚本，如生成索引文件、清理重复内容等
- **GitHub Actions**：实现自动化构建和部署
- **pnpm**：Node.js 包管理器

### 其他技术
- **Git**：版本控制系统
- **Markdown**：文档编写格式

## 环境配置

### 系统要求
- Windows、macOS 或 Linux 操作系统
- 至少 4GB RAM
- 至少 1GB 可用磁盘空间

### 软件依赖

#### 1. Hugo（扩展版）
- **版本要求**：0.146.0 或更高版本（扩展版）
- **安装方法**：
  - **Windows**：使用 Chocolatey 安装 `choco install hugo-extended -y`，或从 [Hugo 官网](https://gohugo.io/getting-started/installing/) 下载二进制文件
  - **macOS**：使用 Homebrew 安装 `brew install hugo`
  - **Linux**：使用包管理器安装，如 Ubuntu 上 `sudo apt-get install hugo`，或从官网下载二进制文件
- **验证安装**：运行 `hugo version`，确保输出包含 "extended"

#### 2. Node.js 和 pnpm
- **Node.js 版本要求**：16.x 或更高版本
- **pnpm 版本要求**：10.x 或更高版本
- **安装方法**：
  - 首先安装 Node.js，从 [Node.js 官网](https://nodejs.org/) 下载并安装
  - 然后安装 pnpm：`npm install -g pnpm`
- **验证安装**：运行 `node -v` 和 `pnpm -v` 查看版本

#### 3. Python 3
- **版本要求**：3.6 或更高版本
- **安装方法**：从 [Python 官网](https://www.python.org/) 下载并安装，或使用系统包管理器
- **验证安装**：运行 `python --version` 或 `python3 --version`

#### 4. Git
- **版本要求**：2.x 或更高版本
- **安装方法**：从 [Git 官网](https://git-scm.com/) 下载并安装，或使用系统包管理器
- **验证安装**：运行 `git --version`

## 安装步骤

### 1. 克隆仓库

```bash
# 克隆仓库到本地
git clone https://github.com/DLCNCC/laws.git
# 进入项目目录
cd index
```

### 2. 安装 Node.js 依赖

```bash
# 使用 pnpm 安装依赖
pnpm install
```

### 3. 安装 Hugo 模块依赖

```bash
# 更新并整理 Hugo 模块依赖
hugo mod get -u && hugo mod tidy
```

### 4. 验证安装

```bash
# 启动本地开发服务器
hugo server -D
```

如果安装成功，你应该能看到类似以下输出：
```
Start building sites …
hugo v0.146.0+extended windows/amd64 BuildDate=2024-05-21T12:08:26Z VendorInfo=gohugoio

                   | EN 
-------------------+----->
  Pages            | 1000
  Paginator pages  |    0
  Non-page files   |    0
  Static files     |  100
  Processed images |    0
  Aliases          |    0
  Sitemaps         |    1
  Cleaned          |    0

Built in 1000 ms
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

现在你可以通过浏览器访问 http://localhost:1313/ 查看网站效果。

## 使用方法

### 1. 启动本地开发服务器

```bash
# 启动本地开发服务器，包含草稿内容
hugo server -D

# 启动本地开发服务器，禁用快速渲染模式（用于调试）
hugo server --disableFastRender

# 指定端口启动
hugo server -p 8080 -D
```

启动后，通过浏览器访问 http://localhost:1313/ 查看网站效果。开发服务器会实时监听文件变化，并自动刷新页面。

### 2. 构建生产版本

```bash
# 构建生产版本
hugo --gc --minify

# 构建并指定基础 URL
hugo --gc --minify --baseURL https://your-domain.com/
```

构建完成后，生成的静态文件将位于 `public` 目录中，可以部署到任何静态网站托管服务。

### 3. 管理内容

#### 添加新的法律法规文档

1. 在 `content` 目录下的相应分类中创建 Markdown 文件
2. 文件命名建议使用中文全称，如 `中华人民共和国宪法.md`
3. 在文件头部添加 YAML 前置元数据，示例：

```yaml
---
title: 中华人民共和国宪法
linkTitle: 宪法
type: "docs"
date: 2023-01-01
---
```

4. 在前置元数据下方编写文档内容，使用 Markdown 格式

#### 自动生成索引文件

项目提供了 Python 脚本来自动生成目录索引文件（`_index.md`），确保文档能够正确显示在导航菜单中。

```bash
# 运行脚本生成索引文件
python create_index_files.py
```

#### 清理重复内容

使用提供的 Python 脚本清理重复的目录或内容：

```bash
# 清理重复的目录索引文件
python clean_duplicate_toc.py

# 清理重复的 YAML 元数据
python fix_duplicate_yaml.py

# 统一 Markdown 格式
python unify_markdown_format.py
```

### 4. 使用搜索功能

- **在线搜索**：在网站顶部的搜索框中输入关键词，点击搜索按钮或按 Enter 键
- **离线搜索**：网站支持离线搜索功能，无需网络连接即可使用
- **搜索结果**：搜索结果会显示相关文档的标题和摘要，点击即可查看完整内容

### 5. 主题切换

- 在网站右上角点击主题切换按钮，可以在浅色模式和深色模式之间切换
- 主题偏好会保存在浏览器的本地存储中，下次访问时会自动应用

### 6. 查看阅读时间

- 每篇文档的顶部会显示预计阅读时间，帮助用户合理安排阅读
- 阅读时间基于默认的阅读速度（每分钟 400 字）计算

## 目录结构

项目采用 Hugo 标准目录结构，同时结合了 Docsy 主题的要求，以下是主要目录和文件的说明：

```
├── .github/             # GitHub 配置文件
│   └── workflows/       # GitHub Actions 工作流配置
├── .trae/               # Trae IDE 相关文件
├── _vendor/             # Hugo 模块依赖（自动生成）
├── addlaws/             # 新增法律法规文档（待整合）
├── addlaws_backup/      # 新增法律法规文档备份
├── assets/              # 静态资源文件
│   ├── icons/           # 图标文件
│   └── scss/            # SCSS 样式文件
├── content/             # 主要内容目录
│   ├── about/           # 关于页面
│   ├── 司法解释/        # 司法解释文档
│   ├── 宪法/            # 宪法相关文档
│   ├── 法律/            # 法律文档
│   ├── 监察法规/        # 监察法规文档
│   ├── 行政执法/        # 行政执法相关文档
│   ├── 行政执法合规/    # 行政执法合规文档
│   ├── 行政法规/        # 行政法规文档
│   ├── _index.md        # 首页内容
│   ├── featured-background.webp  # 特色背景图片
│   └── search.md        # 搜索页面配置
├── i18n/                # 国际化配置
│   └── zh-cn.toml       # 中文语言配置
├── layouts/             # 页面布局模板
│   ├── _markup/         # 标记渲染模板
│   ├── _partials/       # 可复用的模板片段
│   ├── docs/            # 文档页面模板
│   ├── 404.html         # 404 错误页面
│   ├── _td-content.html # 内容渲染模板
│   ├── robots.txt       #  robots.txt 模板
│   └── search.html      # 搜索页面模板
├── static/              # 静态文件
│   └── favicons/        # 网站图标
├── .gitignore           # Git 忽略文件配置
├── .npmrc               # npm 配置文件
├── README.md            # 项目说明文档
├── README_Markdown_Format.md  # Markdown 格式说明
├── clean_duplicate_toc.py      # 清理重复目录索引脚本
├── create_index_files.py       # 生成索引文件脚本
├── fix_duplicate_yaml.py       # 修复重复 YAML 脚本
├── go.mod               # Go 模块依赖配置
├── go.sum               # Go 模块依赖校验
├── hugo.toml            # Hugo 主配置文件
├── package.json         # Node.js 项目配置
├── pnpm-lock.yaml       # pnpm 依赖锁文件
├── unify_markdown_format.py    # 统一 Markdown 格式脚本
├── url_mapping.yaml     # URL 映射配置
├── 添加新法律文件指南.md      # 添加新法律文件指南
└── 部署文档.md          # 部署说明文档
```

### 主要目录说明

#### 1. content/
这是项目的核心内容目录，包含了所有的法律法规文档。文档按照领域和类别进行分层组织，便于浏览和查找。每个子目录都包含一个 `_index.md` 文件，用于定义该目录的元数据和导航信息。

#### 2. layouts/
包含了网站的所有页面布局模板，使用 Hugo 的模板语言编写。这些模板定义了页面的结构和外观，包括头部、导航栏、侧边栏、内容区域和页脚等。

#### 3. assets/
用于存放需要经过 Hugo 处理的静态资源，如 SCSS 样式文件、JavaScript 文件和图像文件等。Hugo 会在构建过程中处理这些资源，生成优化后的静态文件。

#### 4. static/
用于存放不需要经过 Hugo 处理的静态文件，如网站图标、字体文件和第三方库等。这些文件会被直接复制到构建后的 `public` 目录中。

#### 5. i18n/
包含了网站的国际化配置文件，支持多语言功能。目前项目主要使用中文，配置文件为 `zh-cn.toml`。

#### 6. .github/workflows/
包含了 GitHub Actions 工作流配置文件，用于实现自动化构建和部署。当前配置了定时构建和手动触发构建两种方式。

### 关键文件说明

#### 1. hugo.toml
Hugo 的主配置文件，包含了网站的基本设置、语言配置、模块配置、输出配置和各种参数设置等。

#### 2. go.mod 和 go.sum
Go 模块依赖配置文件，用于管理 Hugo 模块的依赖关系。

#### 3. package.json 和 pnpm-lock.yaml
Node.js 项目配置文件，用于管理前端依赖包。

#### 4. Python 脚本
- `create_index_files.py`：自动生成目录索引文件（`_index.md`）
- `clean_duplicate_toc.py`：清理重复的目录索引文件
- `fix_duplicate_yaml.py`：修复重复的 YAML 元数据
- `unify_markdown_format.py`：统一 Markdown 格式

这些脚本用于自动化管理文档内容，提高文档管理效率。

#### 5. README_Markdown_Format.md 和 添加新法律文件指南.md
提供了 Markdown 格式说明和添加新法律文件的指南，帮助用户按照规范添加和编辑文档。

## 贡献指南

欢迎您为「数智法度」项目做出贡献！我们非常感谢社区的支持和参与。以下是贡献指南，帮助您了解如何参与项目。

### 贡献方式

您可以通过以下方式为项目做出贡献：

1. **报告问题**：如果您发现了 bug 或有改进建议，欢迎在 GitHub Issues 中提交
2. **提交代码**：通过 Pull Request 提交修复或新功能
3. **完善文档**：帮助改进项目文档，包括 README.md 和其他说明文件
4. **添加内容**：添加新的法律法规文档或更新现有文档
5. **翻译内容**：将文档翻译成其他语言（如有需要）

### 代码规范

1. **Hugo 模板**：遵循 Hugo 模板最佳实践，保持代码简洁和可读性
2. **SCSS 样式**：遵循 SCSS 最佳实践，使用变量和模块化设计
3. **Python 脚本**：遵循 PEP 8 代码规范，添加适当的注释
4. **Markdown 格式**：遵循项目的 Markdown 格式规范，使用 `unify_markdown_format.py` 脚本统一格式

### 提交流程

1. **Fork 仓库**：在 GitHub 上 Fork 项目仓库到您的个人账号
2. **克隆仓库**：将 Fork 后的仓库克隆到本地
3. **创建分支**：创建一个新的分支用于您的贡献
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **进行修改**：在本地进行代码或内容修改
5. **运行测试**：确保您的修改不会破坏现有功能
   ```bash
   # 启动本地开发服务器，检查网站是否正常运行
   hugo server -D
   ```
6. **提交修改**：提交您的修改，使用清晰的提交信息
   ```bash
   git add .
   git commit -m "添加：新功能描述"
   ```
7. **推送分支**：将您的分支推送到 GitHub
   ```bash
   git push origin feature/your-feature-name
   ```
8. **创建 Pull Request**：在 GitHub 上创建 Pull Request，描述您的修改内容和目的

### 添加新的法律法规文档

1. **选择分类**：确定文档所属的领域和分类
2. **创建文件**：在 `content` 目录下的相应分类中创建 Markdown 文件
3. **添加元数据**：在文件头部添加 YAML 前置元数据，包括标题、链接标题、类型等
4. **编写内容**：使用 Markdown 格式编写文档内容
5. **生成索引**：运行 `create_index_files.py` 脚本确保索引文件正确生成
6. **检查格式**：运行 `unify_markdown_format.py` 脚本统一 Markdown 格式

### 报告问题

当您报告问题时，请提供以下信息：

1. 问题描述：清晰描述您遇到的问题
2. 复现步骤：详细说明如何复现问题
3. 预期结果：您期望的正常行为
4. 实际结果：当前的错误行为
5. 环境信息：包括操作系统、浏览器、Hugo 版本等
6. 截图或日志：如有可能，提供相关截图或错误日志

### 审核流程

1. 提交 Pull Request 后，项目维护者会进行审核
2. 审核过程中可能会提出修改建议，需要您进行相应修改
3. 审核通过后，您的贡献会被合并到主分支
4. 合并后，GitHub Actions 会自动构建和部署网站

### 行为准则

请遵守以下行为准则，确保社区的友好和包容：

1. 尊重他人，不使用侮辱性语言
2. 接受建设性批评
3. 关注社区的最大利益
4. 友善对待其他贡献者

感谢您的贡献！

## 许可证

本项目采用 ISC 许可证。详情请查看 [ISC 许可证](https://opensource.org/licenses/ISC)。

### 数据来源声明

本项目收集的法律法规文档数据来源于：
- 国家法律法规数据库 (https://flk.npc.gov.cn/index)
- 国家规章库 (https://www.gov.cn/zhengce/xxgk/gjgzk/index.htm)

所有法律法规文档的版权归原发布机构所有，本项目仅用于学习和研究目的。

## 联系方式

### 项目地址

- **GitHub 仓库**：https://github.com/DLCNCC/laws
- **项目官网**：https://lawnav.github.io/

### 反馈与建议

- **GitHub Issues**：https://github.com/DLCNCC/laws/issues
- **提交 Bug**：https://github.com/DLCNCC/laws/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=
- **功能请求**：https://github.com/DLCNCC/laws/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.md&title=

### 维护者

- **数智未来**：https://diglit.cn
- **DLCN.CC**：https://www.dlcn.cc

### 贡献者

感谢所有为项目做出贡献的开发者和用户！

## 致谢

- 感谢 Hugo 提供强大的静态网站生成功能
- 感谢 Docsy 主题提供优秀的文档网站模板
- 感谢所有开源工具和库的开发者
- 感谢社区的支持和贡献
