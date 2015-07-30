#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-bones
Version  : 3.8.3
Release  : 1
URL      : https://rubygems.org/downloads/bones-3.8.3.gem
Source0  : https://rubygems.org/downloads/bones-3.8.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-bones-bin
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
Mr Bones
by Tim Pease
https://rubygems.org/gems/bones
== DESCRIPTION:
Mr Bones is a handy tool that creates new Ruby projects from a code
skeleton. The skeleton contains some starter code and a collection of rake
tasks to ease the management and deployment of your source code. Several Mr
Bones plugins are available for creating git repositories, creating GitHub
projects, running various test suites and source code analysis tools.

%package bin
Summary: bin components for the rubygem-bones package.
Group: Binaries

%description bin
bin components for the rubygem-bones package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n bones-3.8.3
gem spec %{SOURCE0} -l --ruby > rubygem-bones.gemspec

%build
gem build rubygem-bones.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
bones-3.8.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/bones-3.8.3.gem
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/AnnotationExtractor/cdesc-AnnotationExtractor.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/AnnotationExtractor/config-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/AnnotationExtractor/display-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/AnnotationExtractor/enumerate-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/AnnotationExtractor/extract_annotations_from-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/AnnotationExtractor/find-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/AnnotationExtractor/id-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/AnnotationExtractor/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/AnnotationExtractor/tag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/ClassMethods/description-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/ClassMethods/option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/ClassMethods/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/ClassMethods/summary-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/ClassMethods/synopsis-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/cdesc-Command.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/config-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/in_directory-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/inherited-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/mrbones_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/output_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/repository-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/skeleton_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/standard_options-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/standard_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/stderr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/stdout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Command/verbose%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Create/announce-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Create/cdesc-Create.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Create/copy_files-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Create/fixme-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Create/in_output_directory-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Create/initialize_create-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Create/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Create/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/_checkout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/_cp-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/_erb-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/_erb_binding-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/_files_to_copy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/_rename-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/archive-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/archive_destination-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/archiving-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/cdesc-FileManager.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/copy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/creating-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/destination%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/destination-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/obj/cdesc-obj.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/repository%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/repository-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/source-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/template-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/updating-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/verbose%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/FileManager/verbose-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Freeze/cdesc-Freeze.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Freeze/freeze_to_repository-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Freeze/initialize_freeze-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Freeze/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Freeze/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Info/cdesc-Info.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Info/initialize_info-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Info/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Main/cdesc-Main.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Main/help-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Main/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Main/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Main/stderr-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Main/stdout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Plugins/all%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Plugins/cdesc-Plugins.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Plugins/find_bones_plugins-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Plugins/find_gemspecs-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Plugins/initialize_plugins-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Plugins/installed%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Plugins/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Plugins/show_plugin-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Unfreeze/cdesc-Unfreeze.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Unfreeze/initialize_unfreeze-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Unfreeze/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/Unfreeze/run-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/cdesc-App.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/App/run-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Colors/cdesc-Colors.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Colors/colorize%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Colors/colorize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/GemPackageTask/cdesc-GemPackageTask.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/GemPackageTask/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/GemPackageTask/gem_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/GemPackageTask/gem_spec-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/GemPackageTask/init-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/GemPackageTask/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Helpers/Rake/cdesc-Rake.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Helpers/cdesc-Helpers.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Helpers/find_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Helpers/have%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Helpers/paragraphs_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Helpers/quiet-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Helpers/remove_desc_for_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Ann/Syntax/cdesc-Syntax.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Ann/Syntax/use_gmail-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Ann/cdesc-Ann.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Ann/define_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Ann/initialize_ann-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Ann/post_load-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/BonesPlugin/Syntax/cdesc-Syntax.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/BonesPlugin/Syntax/enable_sudo-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/BonesPlugin/cdesc-BonesPlugin.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/BonesPlugin/define_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/BonesPlugin/initialize_bones_plugin-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/BonesPlugin/post_load-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Gem/Syntax/cdesc-Syntax.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Gem/Syntax/depend_on-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Gem/Syntax/source-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Gem/cdesc-Gem.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Gem/define_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Gem/import_gemspec-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Gem/initialize_gem-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Gem/load_gemspec-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Gem/manifest-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Gem/post_load-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Notes/cdesc-Notes.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Notes/define_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Notes/initialize_notes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Rdoc/cdesc-Rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Rdoc/define_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Rdoc/initialize_rdoc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Rdoc/post_load-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Rdoc/rdoc_config-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Test/cdesc-Test.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Test/define_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Test/initialize_test-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/Test/post_load-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/Plugins/cdesc-Plugins.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/cdesc-Bones.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/config-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/help-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/libpath-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/path-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Bones/version-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Kernel/Bones-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Kernel/cdesc-Kernel.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Object/alias_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Object/ensure_in_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Object/override_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Object/remove_task-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Object/remove_tasks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Object/valid%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/Rake/cdesc-Rake.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/default/page-version_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/page-History_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/spec/data/page-markdown_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/bones-3.8.3/ri/spec/data/page-rdoc_txt.ri
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/.autotest
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/History.txt
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/bin/bones
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/default/.bnsignore
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/default/History.txt.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/default/README.md.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/default/Rakefile.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/default/bin/NAME.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/default/lib/NAME.rb.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/default/spec/NAME_spec.rb.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/default/spec/spec_helper.rb.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/default/test/test_NAME.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/default/version.txt
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/annotation_extractor.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/app.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/app/command.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/app/create.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/app/file_manager.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/app/freeze.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/app/info.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/app/plugins.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/app/unfreeze.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/colors.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/gem_package_task.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/helpers.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/plugins/ann.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/plugins/bones_plugin.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/plugins/gem.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/plugins/notes.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/plugins/rdoc.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/plugins/test.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/lib/bones/rake_override_task.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/script/bootstrap
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/bones/app/file_manager_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/bones/app_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/bones/helpers_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/bones_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/default/.bnsignore
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/default/.rvmrc.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/default/History
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/default/NAME/NAME.rb.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/default/README.md.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/default/Rakefile.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/default/bin/NAME.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/default/lib/NAME.rb.bns
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/foo/README.md
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/foo/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/markdown.txt
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/data/rdoc.txt
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/bones-3.8.3/version.txt
/usr/lib64/ruby/gems/2.2.0/specifications/bones-3.8.3.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/bones
